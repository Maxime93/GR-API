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
	"name" text NOT NULL,
	"sellin" integer NOT NULL,
	"quality" integer NOT NULL,
	"description" text,
	"photo" text,
	"price" NUMBER NOT NULL,
    "category_id" integer NOT NULL,
    "purchased" integer default 0,
	PRIMARY KEY (id),
    FOREIGN KEY (category_id) REFERENCES category(id)
);

CREATE TABLE "account" (
	"id" integer,
	"mail" text NOT NULL,
	PRIMARY KEY (id),
    UNIQUE(id, mail) ON CONFLICT REPLACE
);

CREATE TABLE "cart" (
	"id" integer,
	"account_id" integer,
	"product_id" integer,
	"purchased" integer default 0,
	PRIMARY KEY (id),
	FOREIGN KEY (product_id) REFERENCES product(id)
    FOREIGN KEY (account_id) REFERENCES account(id)
);
