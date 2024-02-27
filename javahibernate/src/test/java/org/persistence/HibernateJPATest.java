package org.persistence;

import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.EntityTransaction;
import jakarta.persistence.Persistence;
import junit.framework.TestCase;

import java.time.LocalDateTime;
import java.util.function.Consumer;

public class HibernateJPATest extends TestCase {
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
        // create a couple of events...
        inTransaction(entityManager -> {
            entityManager.persist(new Event("Our very first event!", LocalDateTime.now()));
            entityManager.persist(new Event("A follow up event", LocalDateTime.now()));
        });

        // now lets pull events from the database and list them
        inTransaction(entityManager -> entityManager.createQuery("select e from Event e", Event.class).getResultList()
                .forEach(event -> System.out.println("Event (" + event.getDate() + ") : " + event.getTitle())));
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
