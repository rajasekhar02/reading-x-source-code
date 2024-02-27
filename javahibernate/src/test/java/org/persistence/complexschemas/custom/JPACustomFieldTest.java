package org.persistence.complexschemas.custom;

import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.EntityTransaction;
import jakarta.persistence.Persistence;
import junit.framework.TestCase;

import java.time.LocalDateTime;
import java.util.Calendar;
import java.util.Date;
import java.util.function.Consumer;

public class JPACustomFieldTest extends TestCase {
    private EntityManagerFactory entityManagerFactory;

    @Override
    protected void setUp() {
        entityManagerFactory = Persistence.createEntityManagerFactory("org.persistence.jpa");
    }

    @Override
    protected void tearDown() {
        entityManagerFactory.close();
    }
    public void testBasicUsage() {
        // create a couple of events..
        inTransaction(entityManager -> {
            Date dt = new Date();
            Calendar c = Calendar.getInstance();
            c.setTime(dt);
            c.add(Calendar.DATE, 1);
            dt = c.getTime();
            entityManager.persist(new Item("pen", new Date(),  new Date()));
            entityManager.persist(new Item("pen 2", new Date(),  dt));
        });

        // now lets pull events from the database and list them
        inTransaction(entityManager -> entityManager.createQuery("select e from Item e", Item.class).getResultList()
                .forEach(item -> System.out.println("Item (" + item.getName() + ") : " + item.getAuctionStart())));
    }

    void inTransaction(Consumer<EntityManager> work) {
        EntityManager entityManager = entityManagerFactory.createEntityManager();
        EntityTransaction transaction = entityManager.getTransaction();
        try (entityManager) {
            transaction.begin();
            work.accept(entityManager);
            transaction.commit();
        } catch (Exception e) {
            if (transaction.isActive()) {
                transaction.rollback();
            }
            throw e;
        }
    }
}
