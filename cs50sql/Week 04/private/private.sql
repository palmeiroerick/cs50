-- drop view "message";
-- drop table "triplets";

-- create view "message" as
-- select group_concat(txt, ' ') as "phrase" from (
--     select substr("sentence", 98, 4) as txt from "sentences" where id = 14
--     union all
--     select substr("sentence", 3, 5) from "sentences" where id = 114
--     union all
--     select substr("sentence", 72, 9) from "sentences" where id = 618
--     union all
--     select substr("sentence", 7, 3) from "sentences" where id = 630
--     union all
--     select substr("sentence", 12, 5) from "sentences" where id = 932
--     union all
--     select substr("sentence", 50, 7) from "sentences" where id = 2230
--     union all
--     select substr("sentence", 44, 10) from "sentences" where id = 2346
--     union all
--     select substr("sentence", 14, 5) from "sentences" where id = 3041
-- );

create table "triplets" (
    sentence int,
    character int,
    length int
);

delete from "triplets";

insert into "triplets" values
(14, 98, 4),
(114, 3, 5),
(618, 72, 9),
(630, 7, 3),
(932, 12, 5),
(2230, 50, 7),
(2346, 44, 10),
(3041, 14, 5);

-- select substr(s.sentence, t.character, t.length) from sentences s
-- join triplets t on t.sentence = s.id;

create view "message" as
select group_concat(substr(s.sentence, t.character, t.length), ' ') as "phrase"
from "sentences" s join "triplets" t on t.sentence = s.id;

-- select "phrase" from "message";
