package com.readwise.demo.services;

import static org.junit.jupiter.api.Assertions.*;

import java.util.List;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import com.readwise.demo.json.Assignment;
import com.readwise.demo.json.AstroResult;

@SpringBootTest
public class AstroServiceTest {
    @Autowired
    private AstroService service;

    @Test
    void getAstronauts() {
        AstroResult result = service.getAstronauts();
        int number = result.getNumber();
        System.out.println(String.format("There are %d people in space", number));
        List<Assignment> people = result.getPeople();
        people.forEach(System.out::println);
        assertAll(
                () -> assertTrue(number >= 0),
                () -> assertEquals(number, people.size()));
    }
}
