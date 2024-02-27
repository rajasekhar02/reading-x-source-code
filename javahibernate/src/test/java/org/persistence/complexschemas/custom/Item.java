package org.persistence.complexschemas.custom;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import jakarta.validation.constraints.NotNull;
import org.persistence.Constants;

import java.util.Date;

@Entity
@org.hibernate.annotations.Check(
        constraints = "AUCTIONSTART < AUCTIONEND"
)
public class Item {
    @Id
    @GeneratedValue(generator = Constants.ID_GENERATOR)
    protected Long id;

    protected String name;
    @NotNull
    protected Date auctionStart;

    @NotNull
    protected  Date auctionEnd;

    public Item() {
    }

    public Item(String name, Date auctionStart, Date auctionEnd) {
        this.name = name;
        this.auctionStart = auctionStart;
        this.auctionEnd = auctionEnd;
    }
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Date getAuctionStart() {
        return auctionStart;
    }

    public void setAuctionStart(Date auctionStart) {
        this.auctionStart = auctionStart;
    }

    public Date getAuctionEnd() {
        return auctionEnd;
    }

    public void setAuctionEnd(Date auctionEnd) {
        this.auctionEnd = auctionEnd;
    }
}
