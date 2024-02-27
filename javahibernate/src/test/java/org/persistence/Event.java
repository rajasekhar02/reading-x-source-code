package org.persistence;

import jakarta.persistence.*;

import java.time.LocalDateTime;

@Entity
@Table(name = "Events")
class Event {
    @Id
    @GeneratedValue
    private int id;

    private String title;

    @Column(name = "eventDate")
    private LocalDateTime date;

    public Event() {
    }

    public Event(String title, LocalDateTime date) {
        this.title = title;
        this.date = date;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public LocalDateTime getDate() {
        return date;
    }

    public void setDate(LocalDateTime date) {
        this.date = date;
    }
}
