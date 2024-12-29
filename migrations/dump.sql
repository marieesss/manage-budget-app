CREATE TABLE "categorie"(
    "id" SERIAL  NOT NULL,
    "type" VARCHAR(255) CHECK
        ("type" IN('expense', 'income')) NOT NULL DEFAULT 'expense',
        "name" VARCHAR(255) NOT NULL,
        "created_at" DATE NOT NULL, 
    "updated_at" DATE
);
ALTER TABLE
    "categorie" ADD PRIMARY KEY("id");
ALTER TABLE "categorie"
ADD CONSTRAINT "categorie_type_name_unique" UNIQUE ("type", "name");
CREATE TABLE "transaction"(
    "id" SERIAL  NOT NULL,
    "budget_id" BIGINT NOT NULL,
    "categorie_id" BIGINT,
    "amount" DECIMAL(10, 2) NOT NULL,
    "transaction_date" DATE NOT NULL,
    "comment" VARCHAR(255),
    "type" VARCHAR(255) CHECK
        ("type" IN('expense', 'income')) NOT NULL,
    "created_at" DATE NOT NULL, 
    "updated_at" DATE
);
ALTER TABLE
    "transaction" ADD PRIMARY KEY("id");
CREATE TABLE "budget"(
    "id" SERIAL NOT NULL,
    "user_id" BIGINT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "created_at" DATE NOT NULL, 
    "updated_at" DATE
);
ALTER TABLE
    "budget" ADD PRIMARY KEY("id");
CREATE TABLE "user"(
    "id" SERIAL NOT NULL,
    "firstname" VARCHAR(255) NULL,
    "lastname" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255) NOT NULL,
    "password" VARCHAR(255) NOT NULL,
    "created_at" DATE NOT NULL, 
    "updated_at" DATE
);
ALTER TABLE
    "user" ADD PRIMARY KEY("id");
ALTER TABLE
    "user" ADD CONSTRAINT "user_email_unique" UNIQUE("email");
ALTER TABLE
    "budget" ADD CONSTRAINT "budget_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "user"("id");
ALTER TABLE
    "transaction" ADD CONSTRAINT "transaction_categorie_id_foreign" FOREIGN KEY("categorie_id") REFERENCES "categorie"("id");
ALTER TABLE
    "transaction" ADD CONSTRAINT "transaction_budget_id_foreign" FOREIGN KEY("budget_id") REFERENCES "budget"("id");

CREATE TABLE "budget_objective" (
    "id" SERIAL NOT NULL,
    "budget_id" BIGINT NOT NULL,
    "categorie_id" BIGINT NOT NULL,
    "amount" DECIMAL(5, 2) NOT NULL,
    "created_at" DATE NOT NULL,
    "updated_at" DATE,
    PRIMARY KEY ("id"),
    FOREIGN KEY ("budget_id") REFERENCES "budget"("id"),
    FOREIGN KEY ("categorie_id") REFERENCES "categorie"("id")
);
