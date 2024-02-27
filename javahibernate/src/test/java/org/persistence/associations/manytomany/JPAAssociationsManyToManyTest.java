package org.persistence.associations.manytomany;

import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.EntityTransaction;
import jakarta.persistence.Persistence;
import junit.framework.TestCase;

import java.util.Date;
import java.util.function.Consumer;

public class JPAAssociationsManyToManyTest extends TestCase {
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
//        EntityManager entityManager = entityManagerFactory.createEntityManager();
//        EntityTransaction transaction = entityManager.getTransaction();
//        try {
//            transaction.begin();
//            Category someCategory = new Category("Some Category");
//            Category otherCategory = new Category("Other Category");
//            Item someItem = new Item("Some Item");
//            Item otherItem = new Item("Other Item");
//
//            someCategory.getItems().add(someItem);
//            someItem.getCategories().add(someCategory);
//
//            someCategory.getItems().add(otherItem);
//            otherItem. assertEquals(category1.getItems().size(), 2);
//            assertEquals(item1.getCategories().size(), 2);
//
//            assertEquals(category2.getItems().size(), 1);
//            assertEquals(item2.getCategories().size(), 1);
//
//            assertEquals(category2.getItems().iterator().next(), item1);
//            assertEquals(item2.getCategories().iterator().next(), category1);
//getCategories().add(someCategory);
//
//            otherCategory.getItems().add(someItem);
//            someItem.getCategories().add(otherCategory);
//
//            entityManager.persist(someCategory);
//            entityManager.persist(otherCategory);
//            transaction.commit();
//            entityManager.close();
//
//            Long CATEGORY_ID = someCategory.getId();
//            Long OTHER_CATEGORY_ID = otherCategory.getId();
//            Long ITEM_ID = someItem.getId();
//            Long OTHER_ITEM_ID = otherItem.getId();
//            entityManager = entityManagerFactory.createEntityManager();
//            transaction = entityManager.getTransaction();
//
//            transaction.begin();
//            Category category1 = entityManager.find(Category.class, CATEGORY_ID);
//            Category category2 = entityManager.find(Category.class, OTHER_CATEGORY_ID);
//
//            Item item1 = entityManager.find(Item.class, ITEM_ID);
//            Item item2 = entityManager.find(Item.class, OTHER_ITEM_ID);
//
//            assertEquals(category1.getItems().size(), 2);
//            assertEquals(item1.getCategories().size(), 2);
//
//            assertEquals(category2.getItems().size(), 1);
//            assertEquals(item2.getCategories().size(), 1);
//
//            assertEquals(category2.getItems().iterator().next(), item1);
//            assertEquals(item2.getCategories().iterator().next(), category1);
//
//            transaction.commit();
//
//
//        } catch (Exception e) {
//            if (transaction.isActive()) {
//                transaction.rollback();
//            }
//            throw e;
//        } finally {
//            entityManager.close();
//        }
    }

    public void testLinkUsage(){
        EntityManager entityManager = entityManagerFactory.createEntityManager();
        EntityTransaction transaction = entityManager.getTransaction();
        try {
            transaction.begin();
            Category someCategory = new Category("Some Category");
            Category otherCategory = new Category("Other Category");
            entityManager.persist(someCategory);
            entityManager.persist(otherCategory);
            Item someItem = new Item("Some Item");
            Item otherItem = new Item("Other Item");
            entityManager.persist(someItem);
            entityManager.persist(otherItem);

            CategorizedItem linkOne = new CategorizedItem(
                    "johndoe", someCategory, someItem
            );

            CategorizedItem linkTwo = new CategorizedItem(
                    "johndoe", someCategory, otherItem
            );

            CategorizedItem linkThree = new CategorizedItem(
                    "johndoe", otherCategory, someItem
            );

//            entityManager.persist(linkOne);
//            entityManager.persist(linkTwo);
//            entityManager.persist(linkThree);

            transaction.commit();
            entityManager.close();

            Long CATEGORY_ID = someCategory.getId();
            Long OTHER_CATEGORY_ID = otherCategory.getId();
            Long ITEM_ID = someItem.getId();
            Long OTHER_ITEM_ID = otherItem.getId();
            entityManager = entityManagerFactory.createEntityManager();
            transaction = entityManager.getTransaction();

            transaction.begin();
            Category category1 = entityManager.find(Category.class, CATEGORY_ID);
            Category category2 = entityManager.find(Category.class, OTHER_CATEGORY_ID);

            Item item1 = entityManager.find(Item.class, ITEM_ID);
            Item item2 = entityManager.find(Item.class, OTHER_ITEM_ID);

            assertEquals(category1.getCategorizedItems().size(), 2);
            assertEquals(item1.getCategorizedItems().size(), 2);

            assertEquals(category2.getCategorizedItems().size(), 1);
            assertEquals(item2.getCategorizedItems().size(), 1);

            assertEquals(category2.getCategorizedItems().iterator().next().getItem(), item1);
            assertEquals(item2.getCategorizedItems().iterator().next().getCategory(), category1);

            transaction.commit();


        } catch (Exception e) {
            if (transaction.isActive()) {
                transaction.rollback();
            }
            throw e;
        } finally {
            entityManager.close();
        }
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
