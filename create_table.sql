-- Table: public.signal

-- DROP TABLE public.signal;

CREATE TABLE public.signal
(
    channel character varying(200)[] COLLATE pg_catalog."default",
    detail json NOT NULL,
    ts timestamp with time zone
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.signal
    OWNER to postgres;
COMMENT ON TABLE public.signal
    IS 'signal';

-- Index: index_channel

-- DROP INDEX public.index_channel;

CREATE INDEX index_channel
    ON public.signal USING btree
    (channel COLLATE pg_catalog."default")
    TABLESPACE pg_default;