package com.readwise.demo;

import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertSame;
import static org.junit.jupiter.api.Assertions.assertThrows;

import java.util.Arrays;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.NoSuchBeanDefinitionException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.context.ApplicationContext;

import com.readwise.demo.json.Greeting;

@SpringBootTest
class DemoApplicationTests {

	@Autowired
	private ApplicationContext context;

	@Test
	void contextLoads() {
		assertNotNull(context);
		int count = context.getBeanDefinitionCount();
		System.out.println("There are " + count + " beans in the application context");
		Arrays.stream(context.getBeanDefinitionNames()).forEach(System.out::println);
	}

	@Test
	@Disabled
	void noGreetingInAppCtx() {
		assertThrows(NoSuchBeanDefinitionException.class, () -> context.getBean(Greeting.class));
	}

	@Test
	void getBeanTwice() {
		Greeting greeting1 = context.getBean("defaultGreeting", Greeting.class);
		Greeting greeting2 = context.getBean("defaultGreeting", Greeting.class);
		assertSame(greeting1, greeting2);
		System.out.println(greeting2.getMessage());
	}
}
