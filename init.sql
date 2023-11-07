-- create the table if not exists
CREATE TABLE IF NOT EXISTS public.books
(
    id uuid DEFAULT gen_random_uuid(),
    name character varying(255) COLLATE pg_catalog."default"
);

-- create some entries
INSERT INTO books (name) VALUES ('Da Vinci Code');
INSERT INTO books (name) VALUES ('Astérix et Obélix');