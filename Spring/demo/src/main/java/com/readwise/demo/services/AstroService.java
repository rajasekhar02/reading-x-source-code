package com.readwise.demo.services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.web.client.RestTemplateBuilder;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import com.readwise.demo.json.AstroResult;

@Service
public class AstroService {
    private final RestTemplate template;

    @Autowired
    public AstroService(RestTemplateBuilder rtBuilder) {
        template = rtBuilder.build();
    }

    public AstroResult getAstronauts() {
        String url = "http://api.open-notify.org/astros.json";
        return template.getForObject(url, AstroResult.class);
    }
}
