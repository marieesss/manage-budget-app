CREATE TABLE "categorie"(
    "id" SERIAL  NOT NULL,
    "budget_id" BIGINT NULL,
    "type" VARCHAR(255) CHECK
        ("type" IN('expense', 'income')) NOT NULL DEFAULT 'expense',
        "name" VARCHAR(255) NOT NULL,
        "created_at" DATE NOT NULL, 
    "updated_at" DATE
);
ALTER TABLE
    "categorie" ADD PRIMARY KEY("id");
CREATE TABLE "transaction"(
    "id" SERIAL  NOT NULL,
    "budget_id" BIGINT NOT NULL,
    "categorie_id" BIGINT NOT NULL,
    "amount" DECIMAL(10, 2) NOT NULL,
    "transaction_date" DATE NOT NULL,
    "type" VARCHAR(255) CHECK
        ("type" IN('expense', 'income')) NOT NULL,
    "created_at" DATE NOT NULL, 
    "updated_at" DATE
);
ALTER TABLE
    "transaction" ADD PRIMARY KEY("id");
CREATE TABLE "Budget"(
    "id" SERIAL NOT NULL,
    "user_id" BIGINT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "created_at" DATE NOT NULL, 
    "updated_at" DATE
);
ALTER TABLE
    "Budget" ADD PRIMARY KEY("id");
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
    "Budget" ADD CONSTRAINT "budget_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "user"("id");
ALTER TABLE
    "transaction" ADD CONSTRAINT "transaction_categorie_id_foreign" FOREIGN KEY("categorie_id") REFERENCES "categorie"("id");
ALTER TABLE
    "categorie" ADD CONSTRAINT "categorie_budget_id_foreign" FOREIGN KEY("budget_id") REFERENCES "Budget"("id");
ALTER TABLE
    "transaction" ADD CONSTRAINT "transaction_budget_id_foreign" FOREIGN KEY("budget_id") REFERENCES "Budget"("id");


-- Insérer des catégories dans la table "categorie"

-- Catégorie pour les dépenses
INSERT INTO categorie (id,type, name, created_at)
VALUES (1,'expense', 'Food', '1922-02-02'),
       (2, 'expense', 'Transportation', '1922-02-02'),
       (3, 'expense', 'Rent', '1922-02-02'),
       (5,'expense', 'Utilities', '1922-02-02');

-- Catégorie pour les revenus
INSERT INTO categorie (id, type, name, created_at)
VALUES (6, 'income', 'Salary', '1922-02-02'),
       (7, 'income', 'Freelance Income', '1922-02-02');
