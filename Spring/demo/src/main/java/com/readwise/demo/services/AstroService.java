package com.readwise.demo.services;

import java.time.Duration;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.web.client.RestTemplateBuilder;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.reactive.function.client.WebClient;

import com.readwise.demo.json.AstroResult;

@Service
public class AstroService {
    private final RestTemplate template;
    private final WebClient client;
    private final String API_URL;

    @Autowired
    public AstroService(RestTemplateBuilder rtBuilder, WebClient.Builder wcBuilder) {
        API_URL = "http://api.open-notify.org";
        template = rtBuilder.build();
        client = wcBuilder.baseUrl(API_URL).build();
    }

    public AstroResult getAstronauts() {
        return template.getForObject(API_URL+"/astros.json", AstroResult.class);
    }

    public AstroResult getAstronautsWC(){
        return client.get().uri("/astros.json")
        .accept(MediaType.APPLICATION_JSON).retrieve()
        .bodyToMono(AstroResult.class)
        .block(Duration.ofSeconds(2));
    }
}
