package org.persistence.complexschemas.custom;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import org.persistence.Constants;

@Entity(name="User")
public class User{

    @Id
    @GeneratedValue(generator = Constants.ID_GENERATOR)
    protected Long id;
    @Column(
            nullable=false,
            unique=true,
            columnDefinition="EMAIL_ADDRESS(255)"
    )
    protected String email;

    @Column(
            columnDefinition =
                    "varchar(15) not null unique"+
                            " check (not substring(lower(USERNAME), 0, 5) = 'admin')"
    )
    protected String username;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
}