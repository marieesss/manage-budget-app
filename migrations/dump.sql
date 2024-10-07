CREATE TABLE "categorie"(
    "id" BIGINT NOT NULL,
    "budget_id" BIGINT NULL,
    "type" VARCHAR(255) CHECK
        ("type" IN('expense', 'income')) NOT NULL DEFAULT 'expense',
        "name" CHAR(255) NOT NULL
);
ALTER TABLE
    "categorie" ADD PRIMARY KEY("id");
CREATE TABLE "transaction"(
    "transaction_id" BIGINT NOT NULL,
    "budget_id" BIGINT NOT NULL,
    "categorie_id" BIGINT NOT NULL,
    "amount" DECIMAL(10, 2) NOT NULL,
    "transaction_date" DATE NOT NULL,
    "type" VARCHAR(255) CHECK
        ("type" IN('expense', 'income')) NOT NULL
);
ALTER TABLE
    "transaction" ADD PRIMARY KEY("transaction_id");
CREATE TABLE "Budget"(
    "id" BIGINT NOT NULL,
    "user_id" BIGINT NOT NULL,
    "name" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Budget" ADD PRIMARY KEY("id");
CREATE TABLE "user"(
    "user_id" BIGINT NOT NULL,
    "firstname" CHAR(255) NOT NULL,
    "lastname" CHAR(255) NOT NULL,
    "email" CHAR(255) NOT NULL,
    "password" CHAR(255) NOT NULL,
    "creation_date" DATE NOT NULL
);
ALTER TABLE
    "user" ADD PRIMARY KEY("user_id");
ALTER TABLE
    "user" ADD CONSTRAINT "user_email_unique" UNIQUE("email");
ALTER TABLE
    "Budget" ADD CONSTRAINT "budget_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "user"("user_id");
ALTER TABLE
    "transaction" ADD CONSTRAINT "transaction_categorie_id_foreign" FOREIGN KEY("categorie_id") REFERENCES "categorie"("id");
ALTER TABLE
    "categorie" ADD CONSTRAINT "categorie_budget_id_foreign" FOREIGN KEY("budget_id") REFERENCES "Budget"("id");
ALTER TABLE
    "transaction" ADD CONSTRAINT "transaction_budget_id_foreign" FOREIGN KEY("budget_id") REFERENCES "Budget"("id");


-- Insérer des catégories dans la table "categorie"

-- Catégorie pour les dépenses
INSERT INTO categorie (id,type, name)
VALUES (1,'expense', 'Food'),
       (2, 'expense', 'Transportation'),
       (3, 'expense', 'Rent'),
       (5,'expense', 'Utilities');

-- Catégorie pour les revenus
INSERT INTO categorie (id, type, name)
VALUES (6, 'income', 'Salary'),
       (7, 'income', 'Freelance Income');
