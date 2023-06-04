package com.persistence.persistence.dao;

import static org.junit.jupiter.api.Assertions.*;
import static org.hamcrest.Matchers.containsInAnyOrder;
import static org.hamcrest.MatcherAssert.assertThat;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.jdbc.core.JdbcTemplate;

import com.persistence.persistence.entities.Officer;
import com.persistence.persistence.entities.Rank;

import jakarta.transaction.Transactional;

@SpringBootTest
@Transactional
public class JpaOfficerDAOTest {
    @Autowired
    private JpaOfficerDAO dao;

    @Autowired
    private JdbcTemplate template;

    private List<Integer> getIds() {
        return template.query("select id from officers", (rs, num) -> rs.getInt("id"));
    }

    @Test
    public void testSave() {
        Officer officer = new Officer(Rank.LIEUTENANT, "Wesley", "Crusher");
        officer = dao.save(officer);
        assertNotNull(officer.getId());
    }

    @Test
    public void findOneThanExists() {
        getIds().forEach(id -> {
            Optional<Officer> officer = dao.findById(id);
            assertTrue(officer.isPresent());
            assertEquals(id, officer.get().getId());
        });
    }

    @Test
    public void findOneThatDoesNotExist() {
        Optional<Officer> officer = dao.findById(999);
        assertFalse(officer.isPresent());
    }

    @Test
    public void findAll() {
        List<String> dbNames = dao.findAll().stream().map(Officer::getLastName).collect(Collectors.toList());
        assertThat(dbNames, containsInAnyOrder("Archer", "Janeway", "Kirk", "Picard", "Sisko"));
    }

    @Test
    public void count() {
        assertEquals(5, dao.count());
    }

    @Test
    public void delete() {
        getIds().forEach(id -> {
            Optional<Officer> officer = dao.findById(id);
            assertTrue(officer.isPresent());
            dao.delete(officer.get());
        });
        assertEquals(0, dao.count());
    }

    @Test
    public void existsById() {
        getIds().forEach(id -> assertTrue(dao.existsById(id)));
    }
}
