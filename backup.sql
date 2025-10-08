--
-- PostgreSQL database dump
--

\restrict GGTztb2t9N9PqLF0vdnpYxw1YE1AwsYYZDOCvJT9uMR4P0dGJBPmM4Jo0TZO2b4

-- Dumped from database version 15.14 (Debian 15.14-1.pgdg13+1)
-- Dumped by pg_dump version 15.14 (Debian 15.14-1.pgdg13+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: app_user
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO app_user;

--
-- Name: events; Type: TABLE; Schema: public; Owner: app_user
--

CREATE TABLE public.events (
    id integer NOT NULL,
    type character varying,
    repo_name character varying,
    created_at timestamp without time zone,
    user_username character varying
);


ALTER TABLE public.events OWNER TO app_user;

--
-- Name: events_id_seq; Type: SEQUENCE; Schema: public; Owner: app_user
--

CREATE SEQUENCE public.events_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.events_id_seq OWNER TO app_user;

--
-- Name: events_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: app_user
--

ALTER SEQUENCE public.events_id_seq OWNED BY public.events.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: app_user
--

CREATE TABLE public.users (
    username character varying NOT NULL,
    name character varying,
    avatar_url character varying
);


ALTER TABLE public.users OWNER TO app_user;

--
-- Name: events id; Type: DEFAULT; Schema: public; Owner: app_user
--

ALTER TABLE ONLY public.events ALTER COLUMN id SET DEFAULT nextval('public.events_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: app_user
--

COPY public.alembic_version (version_num) FROM stdin;
\.


--
-- Data for Name: events; Type: TABLE DATA; Schema: public; Owner: app_user
--

COPY public.events (id, type, repo_name, created_at, user_username) FROM stdin;
1	PushEvent	pirlo47/TrioCode	2025-10-08 10:03:22.297583	pirlo47
2	PushEvent	pirlo47/TrioCode	2025-10-08 10:03:22.297588	pirlo47
3	PushEvent	pirlo47/TrioCode	2025-10-08 10:03:22.297593	pirlo47
4	PushEvent	pirlo47/TrioCode	2025-10-08 10:03:22.297598	pirlo47
5	PushEvent	pirlo47/TrioCode	2025-10-08 10:03:22.2976	pirlo47
6	WatchEvent	pirlo47/TrioCode	2025-10-08 10:03:22.297604	pirlo47
7	IssuesEvent	pirlo47/Github-UserActivity	2025-10-08 10:03:22.297607	pirlo47
8	PushEvent	pirlo47/TrioCode	2025-10-08 10:03:22.297611	pirlo47
9	PushEvent	pirlo47/TrioCode	2025-10-08 10:03:22.297615	pirlo47
10	PushEvent	pirlo47/TrioCode	2025-10-08 10:03:22.297625	pirlo47
11	PushEvent	pirlo47/TrioCode	2025-10-08 10:03:22.297628	pirlo47
12	CreateEvent	pirlo47/TrioCode	2025-10-08 10:03:22.297632	pirlo47
13	CreateEvent	pirlo47/TrioCode	2025-10-08 10:03:22.297636	pirlo47
14	PushEvent	pirlo47/Phehello-Ntoahae-	2025-10-08 10:03:22.297639	pirlo47
15	PushEvent	pirlo47/Broadcast_Server	2025-10-08 10:03:22.297642	pirlo47
16	PushEvent	SimangaThinkDev/MoreMove---WarmHands	2025-10-08 10:03:22.297646	pirlo47
17	PushEvent	SimangaThinkDev/MoreMove---WarmHands	2025-10-08 10:03:22.29765	pirlo47
18	CreateEvent	pirlo47/Broadcast_Server-	2025-10-08 10:03:22.297653	pirlo47
19	CreateEvent	pirlo47/Broadcast_Server-	2025-10-08 10:03:22.297657	pirlo47
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: app_user
--

COPY public.users (username, name, avatar_url) FROM stdin;
pirlo47	Phehello Ntoahae	https://avatars.githubusercontent.com/u/161002727?v=4
\.


--
-- Name: events_id_seq; Type: SEQUENCE SET; Schema: public; Owner: app_user
--

SELECT pg_catalog.setval('public.events_id_seq', 19, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: app_user
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: events events_pkey; Type: CONSTRAINT; Schema: public; Owner: app_user
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: app_user
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (username);


--
-- Name: ix_events_id; Type: INDEX; Schema: public; Owner: app_user
--

CREATE INDEX ix_events_id ON public.events USING btree (id);


--
-- Name: ix_users_username; Type: INDEX; Schema: public; Owner: app_user
--

CREATE INDEX ix_users_username ON public.users USING btree (username);


--
-- Name: events events_user_username_fkey; Type: FK CONSTRAINT; Schema: public; Owner: app_user
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_user_username_fkey FOREIGN KEY (user_username) REFERENCES public.users(username);


--
-- PostgreSQL database dump complete
--

\unrestrict GGTztb2t9N9PqLF0vdnpYxw1YE1AwsYYZDOCvJT9uMR4P0dGJBPmM4Jo0TZO2b4

