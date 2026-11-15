-- Written by build.py from site_data.PADDLE. Safe to rerun: maps each Paddle price id to what it grants (schema.sql, v11).
insert into public.paddle_prices (price_id, product, tier, period, kind) values
  ('pri_01m7excpcpt20vcx6ck15z0t0n', 'ig-econ', 'basic', 'm', 'student'),
  ('pri_01m7excpmz3e15qptgxsm033nx', 'ig-econ', 'basic', 'y', 'student'),
  ('pri_01m7excrnts2bc3b0cbwm2qzqv', 'ig-cs', 'basic', 'm', 'student'),
  ('pri_01m7excrxdjysc7kaywcr36v1s', 'ig-cs', 'basic', 'y', 'student'),
  ('pri_01m7exctwhrv16n2wfrn8dy04t', 'a-econ', 'basic', 'm', 'student'),
  ('pri_01m7excv48n43qm7d70nhkhaks', 'a-econ', 'basic', 'y', 'student'),
  ('pri_01m7excwfzvqycq52d7w4zvyyd', 'a-cs', 'basic', 'm', 'student'),
  ('pri_01m7excwr6yq9rkffcjdc29tq9', 'a-cs', 'basic', 'y', 'student'),
  ('pri_01m7excqwg12pxrdxy41hka4q0', 'ig-econ', 'full', 'm', 'student'),
  ('pri_01m7excr5198cx8y63v34qzwtj', 'ig-econ', 'full', 'y', 'student'),
  ('pri_01m7excsdp52p2e3cp5ypceh52', 'ig-cs', 'full', 'm', 'student'),
  ('pri_01m7exctb583xtyvcheafrc6a6', 'ig-cs', 'full', 'y', 'student'),
  ('pri_01m7excvnd5f12dp0rwta2ajqd', 'a-econ', 'full', 'm', 'student'),
  ('pri_01m7excvz4td7egsd78vs9kw28', 'a-econ', 'full', 'y', 'student'),
  ('pri_01m7excxanaah3t0npacavm84b', 'a-cs', 'full', 'm', 'student'),
  ('pri_01m7excxk410tzh1kv1pfs4khs', 'a-cs', 'full', 'y', 'student'),
  ('pri_01m7excy50p6h7hkxmbn0jmqqn', 'school-all', 'vip', 'm', 'student'),
  ('pri_01m7excycz8kw9ayvea6svcb5s', 'school-all', 'vip', 'y', 'student'),
  ('pri_01m7exczkbyt8wbdt4sa969bm0', null, 'full', 'm', 'teacher'),
  ('pri_01m7exczvbzf84xms3e743fs4j', null, 'full', 'y', 'teacher')
on conflict (price_id) do update set product = excluded.product, tier = excluded.tier, period = excluded.period, kind = excluded.kind;
delete from public.paddle_prices where price_id not in ('pri_01m7excpcpt20vcx6ck15z0t0n','pri_01m7excpmz3e15qptgxsm033nx','pri_01m7excrnts2bc3b0cbwm2qzqv','pri_01m7excrxdjysc7kaywcr36v1s','pri_01m7exctwhrv16n2wfrn8dy04t','pri_01m7excv48n43qm7d70nhkhaks','pri_01m7excwfzvqycq52d7w4zvyyd','pri_01m7excwr6yq9rkffcjdc29tq9','pri_01m7excqwg12pxrdxy41hka4q0','pri_01m7excr5198cx8y63v34qzwtj','pri_01m7excsdp52p2e3cp5ypceh52','pri_01m7exctb583xtyvcheafrc6a6','pri_01m7excvnd5f12dp0rwta2ajqd','pri_01m7excvz4td7egsd78vs9kw28','pri_01m7excxanaah3t0npacavm84b','pri_01m7excxk410tzh1kv1pfs4khs','pri_01m7excy50p6h7hkxmbn0jmqqn','pri_01m7excycz8kw9ayvea6svcb5s','pri_01m7exczkbyt8wbdt4sa969bm0','pri_01m7exczvbzf84xms3e743fs4j');
