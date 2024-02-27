package org.persistence;

import junit.framework.TestCase;

import org.hibernate.SessionFactory;
import org.hibernate.boot.MetadataSources;
import org.hibernate.boot.registry.StandardServiceRegistry;
import org.hibernate.boot.registry.StandardServiceRegistryBuilder;

import static java.lang.System.out;
import static java.time.LocalDateTime.now;


public class HibernateIllustrationTest extends TestCase {
    private SessionFactory sessionFactory;

    @Override
    protected void setUp() {
        // A SessionFactory is set up once for an application!
        final StandardServiceRegistry registry =
                new StandardServiceRegistryBuilder()
                        .build();
        try {
            sessionFactory =
                    new MetadataSources(registry)
                            .addAnnotatedClass(Event.class)
                            .addAnnotatedClass(Account.class)
                            .buildMetadata()
                            .buildSessionFactory();
        }
        catch (Exception e) {
            // The registry would be destroyed by the SessionFactory, but we
            // had trouble building the SessionFactory so destroy it manually.
            StandardServiceRegistryBuilder.destroy(registry);
        }

    }

    @Override
    protected void tearDown() {
        if ( sessionFactory != null ) {
            sessionFactory.close();
        }
    }

    public void testBasicUsage() {
        // create a couple of events...
        sessionFactory.inTransaction(session -> {
            session.persist(new Event("Our very first event!", now()));
            session.persist(new Event("A follow up event", now()));
        });

        // now lets pull events from the database and list them
        sessionFactory
                .inTransaction(
                        session -> session
                                .createSelectionQuery("from Event", Event.class)
                                .getResultList()
                                .forEach(
                                        event -> out.
                                                println("Event (" + event.getDate() + ") : " + event.getTitle())
                                )
                );
    }

    public void testFormulaUsage(){
        sessionFactory.inTransaction(session -> {
            Account account = new Account();
            account.setId(1L);
            account.setCredit(5000d);
            account.setRate(1.25 / 100);
            session.persist(account);
        });
        sessionFactory.inTransaction(session -> {
            Account account = session.find(Account.class, 1L);
            assertEquals(62.5d, account.getInterest());
        });
    }
}
