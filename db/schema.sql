CREATE TABLE "category" (
	"id" integer,
	"name" test, PRIMARY KEY (id)
);

INSERT INTO category (name)
VALUES ('STANDARD');

INSERT INTO category (name)
VALUES ('BRIE');

INSERT INTO category (name)
VALUES ('SULFURAS');

INSERT INTO category (name)
VALUES ('CONJURED');

CREATE TABLE "product" (
	"id" integer,
	"name" text,
	"sellin" integer,
	"quality" integer,
	"description" text,
	"photo" text,
	"price" NUMBER,
    "category_id" integer,
	PRIMARY KEY (id),
    FOREIGN KEY (category_id) REFERENCES category(id)
);