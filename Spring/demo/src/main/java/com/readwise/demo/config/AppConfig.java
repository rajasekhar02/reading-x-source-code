package com.readwise.demo.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import com.readwise.demo.json.Greeting;

@Configuration
public class AppConfig {
    @Bean
    public Greeting defaultGreeting() {
        return new Greeting("Hello, World");
    }

    @Bean
    public Greeting whatsupGreeting() {
        return new Greeting("whats up");
    }
}
