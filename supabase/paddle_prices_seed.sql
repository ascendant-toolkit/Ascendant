-- Written by build.py from site_data.PADDLE. Safe to rerun: maps each Paddle price id to what it grants (schema.sql, v11).
insert into public.paddle_prices (price_id, product, tier, period, kind) values
  ('pri_01m7f2ehjy375pgwyg4ggj1e6c', 'ig-econ', 'basic', 'm', 'student'),
  ('pri_01m7f2ehw7zearvfn6yga2t6c2', 'ig-econ', 'basic', 'y', 'student'),
  ('pri_01m7f2emyn5myb99kyy3msdhdr', 'ig-cs', 'basic', 'm', 'student'),
  ('pri_01m7f2en9yytq22zm21kkr2ake', 'ig-cs', 'basic', 'y', 'student'),
  ('pri_01m7f2epyjbf5f25j9xd6nzg9q', 'a-econ', 'basic', 'm', 'student'),
  ('pri_01m7f2eq7qr2hx6zcab3qgtr66', 'a-econ', 'basic', 'y', 'student'),
  ('pri_01m7f2erwc5qzthytmw8sjq4ye', 'a-cs', 'basic', 'm', 'student'),
  ('pri_01m7f2es5xbytn2hv7qhdkwf4s', 'a-cs', 'basic', 'y', 'student'),
  ('pri_01m7f2ek84hex1p4r0wpc5efwj', 'ig-econ', 'full', 'm', 'student'),
  ('pri_01m7f2ekj8hqmmetxfrsn3nv42', 'ig-econ', 'full', 'y', 'student'),
  ('pri_01m7f2enyqhqy9fcp6ackq038d', 'ig-cs', 'full', 'm', 'student'),
  ('pri_01m7f2ep8hs4zs5dehfgx1fxdr', 'ig-cs', 'full', 'y', 'student'),
  ('pri_01m7f2eqww8zm7t1vchxmkqqjd', 'a-econ', 'full', 'm', 'student'),
  ('pri_01m7f2er6rehk74hk99x1gmdne', 'a-econ', 'full', 'y', 'student'),
  ('pri_01m7f2est9hcqq1yt9h2w4pjwe', 'a-cs', 'full', 'm', 'student'),
  ('pri_01m7f2et3bpfbqy6zmfzxzhg1n', 'a-cs', 'full', 'y', 'student'),
  ('pri_01m7f2etrcgg6snt0n49car0mj', 'school-all', 'vip', 'm', 'student'),
  ('pri_01m7f2ev2024jk4h05zafdjx2r', 'school-all', 'vip', 'y', 'student'),
  ('pri_01m7f2evpvxqy8pke74q81jfz9', null, 'full', 'm', 'teacher'),
  ('pri_01m7f2ew0gm1mmzvvv00c17kdv', null, 'full', 'y', 'teacher')
on conflict (price_id) do update set product = excluded.product, tier = excluded.tier, period = excluded.period, kind = excluded.kind;
delete from public.paddle_prices where price_id not in ('pri_01m7f2ehjy375pgwyg4ggj1e6c','pri_01m7f2ehw7zearvfn6yga2t6c2','pri_01m7f2emyn5myb99kyy3msdhdr','pri_01m7f2en9yytq22zm21kkr2ake','pri_01m7f2epyjbf5f25j9xd6nzg9q','pri_01m7f2eq7qr2hx6zcab3qgtr66','pri_01m7f2erwc5qzthytmw8sjq4ye','pri_01m7f2es5xbytn2hv7qhdkwf4s','pri_01m7f2ek84hex1p4r0wpc5efwj','pri_01m7f2ekj8hqmmetxfrsn3nv42','pri_01m7f2enyqhqy9fcp6ackq038d','pri_01m7f2ep8hs4zs5dehfgx1fxdr','pri_01m7f2eqww8zm7t1vchxmkqqjd','pri_01m7f2er6rehk74hk99x1gmdne','pri_01m7f2est9hcqq1yt9h2w4pjwe','pri_01m7f2et3bpfbqy6zmfzxzhg1n','pri_01m7f2etrcgg6snt0n49car0mj','pri_01m7f2ev2024jk4h05zafdjx2r','pri_01m7f2evpvxqy8pke74q81jfz9','pri_01m7f2ew0gm1mmzvvv00c17kdv');
