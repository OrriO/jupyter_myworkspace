drop table dev.dev_temp_msj_risk_jdata_feature_user_dim_v3_${suffix};
create table if not exists dev.dev_temp_msj_risk_jdata_feature_user_dim_v3_${suffix} stored as orc as select
	user_month_action.*,
	user_info.`(user_id)?+.+`,
	user_1days_action.`(user_id)?+.+`,
	user_3days_action.`(user_id)?+.+`,
	user_5days_action.`(user_id)?+.+`,
	user_7days_action.`(user_id)?+.+`,
	user_10days_action.`(user_id)?+.+`,
	user_15days_action.`(user_id)?+.+`
from
(
	select user_id,
		sum(case when action_type=1 then 1 else 0 end) as user_month_browse_cnt,
		sum(case when action_type=2 then 1 else 0 end) as user_month_add_cart_cnt,
		sum(case when action_type=3 then 1 else 0 end) as user_month_del_cart_cnt, 
		sum(case when action_type=4 then 1 else 0 end) as user_month_order_cnt, 
		sum(case when action_type=5 then 1 else 0 end) as user_month_focus_cnt,
		sum(case when action_type=6 then 1 else 0 end) as user_month_click_cnt,
		
		count(distinct case when action_type=1 then substring(action_time,1,10) else NULL end) as user_month_browse_day_cnt,
		count(distinct case when action_type=2 then substring(action_time,1,10) else NULL end) as user_month_add_cart_day_cnt,
		count(distinct case when action_type=3 then substring(action_time,1,10) else NULL end) as user_month_del_cart_day_cnt,
		count(distinct case when action_type=4 then substring(action_time,1,10) else NULL end) as user_month_order_day_cnt,
		count(distinct case when action_type=5 then substring(action_time,1,10) else NULL end) as user_month_focus_day_cnt,
		count(distinct case when action_type=6 then substring(action_time,1,10) else NULL end) as user_month_click_day_cnt,
		
		sum(case when action_type=4 then 1 else 0 end)/sum(case when action_type=6 then 1 else 0 end) as user_month_click_buy_rate,
		sum(case when action_type=2 then 1 else 0 end)/sum(case when action_type=6 then 1 else 0 end) as user_month_click_cart_rate,
		sum(case when action_type=5 then 1 else 0 end)/sum(case when action_type=6 then 1 else 0 end) as user_month_click_focus_rate,

		sum(case when action_type=4 then 1 else 0 end)/sum(case when action_type=1 then 1 else 0 end) as user_month_browse_buy_rate,
		sum(case when action_type=4 then 1 else 0 end)/sum(case when action_type=2 then 1 else 0 end) as user_month_cart_buy_rate,
		sum(case when action_type=4 then 1 else 0 end)/sum(case when action_type=5 then 1 else 0 end) as user_month_focus_buy_rate,
		
		count(distinct case when action_type=1 then sku_id else NULL end) as user_month_browse_sku_cnt,
		count(distinct case when action_type=2 then sku_id else NULL end) as user_month_add_cart_sku_cnt,
		count(distinct case when action_type=3 then sku_id else NULL end) as user_month_del_cart_sku_cnt,
		count(distinct case when action_type=4 then sku_id else NULL end) as user_month_order_sku_cnt,
		count(distinct case when action_type=5 then sku_id else NULL end) as user_month_focus_sku_cnt,
		count(distinct case when action_type=6 then sku_id else NULL end) as user_month_click_sku_cnt,
		
		count(distinct case when action_type=1 then action_brand else NULL end) as user_month_browse_brand_cnt,
		count(distinct case when action_type=2 then action_brand else NULL end) as user_month_add_cart_brand_cnt,
		count(distinct case when action_type=3 then action_brand else NULL end) as user_month_del_cart_brand_cnt,
		count(distinct case when action_type=4 then action_brand else NULL end) as user_month_order_brand_cnt,
		count(distinct case when action_type=5 then action_brand else NULL end) as user_month_focus_brand_cnt,
		count(distinct case when action_type=6 then action_brand else NULL end) as user_month_click_brand_cnt,
		
		
		datediff(date_add('${current_date}',1),max(case when action_type=1 then substring(action_time,1,10) else '2016-01-01' end)) as user_month_least_browse_day_cnt,
		datediff(date_add('${current_date}',1),max(case when action_type=2 then substring(action_time,1,10) else '2016-01-01' end)) as user_month_least_add_cart_day_cnt,
		datediff(date_add('${current_date}',1),max(case when action_type=3 then substring(action_time,1,10) else '2016-01-01' end)) as user_month_least_del_cart_day_cnt,
		datediff(date_add('${current_date}',1),max(case when action_type=4 then substring(action_time,1,10) else '2016-01-01' end)) as user_month_least_order_day_cnt,
		datediff(date_add('${current_date}',1),max(case when action_type=5 then substring(action_time,1,10) else '2016-01-01' end)) as user_month_least_focus_day_cnt,
		datediff(date_add('${current_date}',1),max(case when action_type=6 then substring(action_time,1,10) else '2016-01-01' end)) as user_month_least_click_day_cnt,
		
		(30/count(distinct case when action_type=1 then substring(action_time,1,10) else NULL end)+0.1) as user_month_avg_browse_interval_day,
		(30/count(distinct case when action_type=2 then substring(action_time,1,10) else NULL end)+0.1) as user_month_avg_add_cart_interval_day,
		(30/count(distinct case when action_type=3 then substring(action_time,1,10) else NULL end)+0.1) as user_month_avg_del_cart_interval_day,
		(30/count(distinct case when action_type=4 then substring(action_time,1,10) else NULL end)+0.1) as user_month_avg_order_interval_day,
		(30/count(distinct case when action_type=5 then substring(action_time,1,10) else NULL end)+0.1) as user_month_avg_focus_interval_day,
		(30/count(distinct case when action_type=6 then substring(action_time,1,10) else NULL end)+0.1) as user_month_avg_click_interval_day,
		
		sum(case when action_type=1 then 1 else 0 end)/30 as user_month_each_day_avg_browse_cnt,
		sum(case when action_type=2 then 1 else 0 end)/30 as user_month_each_day_avg_add_cart_cnt,
		sum(case when action_type=3 then 1 else 0 end)/30 as user_month_each_day_avg_del_cart_cnt, 
		sum(case when action_type=4 then 1 else 0 end)/30 as user_month_each_day_avg_order_cnt, 
		sum(case when action_type=5 then 1 else 0 end)/30 as user_month_each_day_avg_focus_cnt,
		sum(case when action_type=6 then 1 else 0 end)/30 as user_month_each_day_avg_click_cnt,
		
		count(distinct case when action_type=1 then sku_id else NULL end)/30 as user_month_each_day_avg_browse_sku_cnt,
		count(distinct case when action_type=2 then sku_id else NULL end)/30 as user_month_each_day_avg_add_cart_sku_cnt,
		count(distinct case when action_type=3 then sku_id else NULL end)/30 as user_month_each_day_avg_del_cart_sku_cnt,
		count(distinct case when action_type=4 then sku_id else NULL end)/30 as user_month_each_day_avg_order_sku_cnt,
		count(distinct case when action_type=5 then sku_id else NULL end)/30 as user_month_each_day_avg_focus_sku_cnt,
		count(distinct case when action_type=6 then sku_id else NULL end)/30 as user_month_each_day_avg_click_sku_cnt,
		
		count(distinct case when action_type=1 then action_brand else NULL end)/30 as user_month_each_day_avg_browse_brand_cnt,
		count(distinct case when action_type=2 then action_brand else NULL end)/30 as user_month_each_day_avg_add_cart_brand_cnt,
		count(distinct case when action_type=3 then action_brand else NULL end)/30 as user_month_each_day_avg_del_cart_brand_cnt,
		count(distinct case when action_type=4 then action_brand else NULL end)/30 as user_month_each_day_avg_order_brand_cnt,
		count(distinct case when action_type=5 then action_brand else NULL end)/30 as user_month_each_day_avg_focus_brand_cnt,
		count(distinct case when action_type=6 then action_brand else NULL end)/30 as user_month_each_day_avg_click_brand_cnt
		
	from dev.dev_temp_msj_risk_jdata_action_wide_table 
	where substring(action_time,1,10)>=date_sub('${current_date}',30) and substring(action_time,1,10)<='${current_date}'  and action_cate = 6
	group by user_id
) user_month_action
left outer join
(
		select user_id,cast(user_lv_cd as INT) as user_level,
		cast(case when sex = 'NULL' then -1 else sex end as INT) as sex,
		datediff(date_add('${current_date}',1),user_reg_dt) as reg_day_cnt,
		(case when age = '15?????????' then 1
			when age = '16-25???'  then 2
			when age = '26-35???'  then 3
			when age = '36-45???'  then 4
			when age = '46-55???'  then 5
			when age = '56?????????' then 6
			else 0 end) age_level
		from dev.dev_temp_msj_risk_jdata_user where user_id !='user_id'
)user_info
on user_month_action.user_id = user_info.user_id
left outer join
(
	select user_id,
		sum(case when action_type=1 then 1 else 0 end) as user_1days_browse_cnt,
		sum(case when action_type=2 then 1 else 0 end) as user_1days_add_cart_cnt,
		sum(case when action_type=3 then 1 else 0 end) as user_1days_del_cart_cnt, 
		sum(case when action_type=4 then 1 else 0 end) as user_1days_order_cnt, 
		sum(case when action_type=5 then 1 else 0 end) as user_1days_focus_cnt,
		sum(case when action_type=6 then 1 else 0 end) as user_1days_click_cnt,
		
		sum(case when action_type=4 then 1 else 0 end)/sum(case when action_type=6 then 1 else 0 end) as user_1days_click_buy_rate,
		sum(case when action_type=2 then 1 else 0 end)/sum(case when action_type=6 then 1 else 0 end) as user_1days_click_cart_rate,
		sum(case when action_type=5 then 1 else 0 end)/sum(case when action_type=6 then 1 else 0 end) as user_1days_click_focus_rate,

		sum(case when action_type=4 then 1 else 0 end)/sum(case when action_type=1 then 1 else 0 end) as user_1days_browse_buy_rate,
		sum(case when action_type=4 then 1 else 0 end)/sum(case when action_type=2 then 1 else 0 end) as user_1days_cart_buy_rate,
		sum(case when action_type=4 then 1 else 0 end)/sum(case when action_type=5 then 1 else 0 end) as user_1days_focus_buy_rate,
		
		count(distinct case when action_type=1 then sku_id else NULL end) as user_1days_browse_sku_cnt,
		count(distinct case when action_type=2 then sku_id else NULL end) as user_1days_add_cart_sku_cnt,
		count(distinct case when action_type=3 then sku_id else NULL end) as user_1days_del_cart_sku_cnt,
		count(distinct case when action_type=4 then sku_id else NULL end) as user_1days_order_sku_cnt,
		count(distinct case when action_type=5 then sku_id else NULL end) as user_1days_focus_sku_cnt,
		count(distinct case when action_type=6 then sku_id else NULL end) as user_1days_click_sku_cnt,
		
		count(distinct case when action_type=1 then action_brand else NULL end) as user_1days_browse_brand_cnt,
		count(distinct case when action_type=2 then action_brand else NULL end) as user_1days_add_cart_brand_cnt,
		count(distinct case when action_type=3 then action_brand else NULL end) as user_1days_del_cart_brand_cnt,
		count(distinct case when action_type=4 then action_brand else NULL end) as user_1days_order_brand_cnt,
		count(distinct case when action_type=5 then action_brand else NULL end) as user_1days_focus_brand_cnt,
		count(distinct case when action_type=6 then action_brand else NULL end) as user_1days_click_brand_cnt,
		
		count(distinct case when action_type=1 then substring(action_time,1,10) else NULL end) as user_1days_browse_day_cnt,
		count(distinct case when action_type=2 then substring(action_time,1,10) else NULL end) as user_1days_add_cart_day_cnt,
		count(distinct case when action_type=3 then substring(action_time,1,10) else NULL end) as user_1days_del_cart_day_cnt,
		count(distinct case when action_type=4 then substring(action_time,1,10) else NULL end) as user_1days_order_day_cnt,
		count(distinct case when action_type=5 then substring(action_time,1,10) else NULL end) as user_1days_focus_day_cnt,
		count(distinct case when action_type=6 then substring(action_time,1,10) else NULL end) as user_1days_click_day_cnt
		
	from dev.dev_temp_msj_risk_jdata_action_wide_table 
	where substring(action_time,1,10)='${current_date}'  and action_cate = 6
	group by user_id
) user_1days_action
on user_month_action.user_id = user_1days_action.user_id
left outer join
(
	select user_id,
		sum(case when action_type=1 then 1 else 0 end) as user_3days_browse_cnt,
		sum(case when action_type=2 then 1 else 0 end) as user_3days_add_cart_cnt,
		sum(case when action_type=3 then 1 else 0 end) as user_3days_del_cart_cnt, 
		sum(case when action_type=4 then 1 else 0 end) as user_3days_order_cnt, 
		sum(case when action_type=5 then 1 else 0 end) as user_3days_focus_cnt,
		sum(case when action_type=6 then 1 else 0 end) as user_3days_click_cnt,
		
		sum(case when action_type=4 then 1 else 0 end)/sum(case when action_type=6 then 1 else 0 end) as user_3days_click_buy_rate,
		sum(case when action_type=2 then 1 else 0 end)/sum(case when action_type=6 then 1 else 0 end) as user_3days_click_cart_rate,
		sum(case when action_type=5 then 1 else 0 end)/sum(case when action_type=6 then 1 else 0 end) as user_3days_click_focus_rate,
		
		sum(case when action_type=4 then 1 else 0 end)/sum(case when action_type=1 then 1 else 0 end) as user_3days_browse_buy_rate,
		sum(case when action_type=4 then 1 else 0 end)/sum(case when action_type=2 then 1 else 0 end) as user_3days_cart_buy_rate,
		sum(case when action_type=4 then 1 else 0 end)/sum(case when action_type=5 then 1 else 0 end) as user_3days_focus_buy_rate,
		
		count(distinct case when action_type=1 then sku_id else NULL end) as user_3days_browse_sku_cnt,
		count(distinct case when action_type=2 then sku_id else NULL end) as user_3days_add_cart_sku_cnt,
		count(distinct case when action_type=3 then sku_id else NULL end) as user_3days_del_cart_sku_cnt,
		count(distinct case when action_type=4 then sku_id else NULL end) as user_3days_order_sku_cnt,
		count(distinct case when action_type=5 then sku_id else NULL end) as user_3days_focus_sku_cnt,
		count(distinct case when action_type=6 then sku_id else NULL end) as user_3days_click_sku_cnt,
		
		count(distinct case when action_type=1 then action_brand else NULL end) as user_3days_browse_brand_cnt,
		count(distinct case when action_type=2 then action_brand else NULL end) as user_3days_add_cart_brand_cnt,
		count(distinct case when action_type=3 then action_brand else NULL end) as user_3days_del_cart_brand_cnt,
		count(distinct case when action_type=4 then action_brand else NULL end) as user_3days_order_brand_cnt,
		count(distinct case when action_type=5 then action_brand else NULL end) as user_3days_focus_brand_cnt,
		count(distinct case when action_type=6 then action_brand else NULL end) as user_3days_click_brand_cnt,
		
		count(distinct case when action_type=1 then substring(action_time,1,10) else NULL end) as user_3days_browse_day_cnt,
		count(distinct case when action_type=2 then substring(action_time,1,10) else NULL end) as user_3days_add_cart_day_cnt,
		count(distinct case when action_type=3 then substring(action_time,1,10) else NULL end) as user_3days_del_cart_day_cnt,
		count(distinct case when action_type=4 then substring(action_time,1,10) else NULL end) as user_3days_order_day_cnt,
		count(distinct case when action_type=5 then substring(action_time,1,10) else NULL end) as user_3days_focus_day_cnt,
		count(distinct case when action_type=6 then substring(action_time,1,10) else NULL end) as user_3days_click_day_cnt,
		
		(3/count(distinct case when action_type=1 then substring(action_time,1,10) else NULL end)+0.1) as user_3days_avg_browse_interval_day,
		(3/count(distinct case when action_type=2 then substring(action_time,1,10) else NULL end)+0.1) as user_3days_avg_add_cart_interval_day,
		(3/count(distinct case when action_type=3 then substring(action_time,1,10) else NULL end)+0.1) as user_3days_avg_del_cart_interval_day,
		(3/count(distinct case when action_type=4 then substring(action_time,1,10) else NULL end)+0.1) as user_3days_avg_order_interval_day,
		(3/count(distinct case when action_type=5 then substring(action_time,1,10) else NULL end)+0.1) as user_3days_avg_focus_interval_day,
		(3/count(distinct case when action_type=6 then substring(action_time,1,10) else NULL end)+0.1) as user_3days_avg_click_interval_day,
		
		sum(case when action_type=1 then 1 else 0 end)/3 as user_3days_each_day_avg_browse_cnt,
		sum(case when action_type=2 then 1 else 0 end)/3 as user_3days_each_day_avg_add_cart_cnt,
		sum(case when action_type=3 then 1 else 0 end)/3 as user_3days_each_day_avg_del_cart_cnt, 
		sum(case when action_type=4 then 1 else 0 end)/3 as user_3days_each_day_avg_order_cnt, 
		sum(case when action_type=5 then 1 else 0 end)/3 as user_3days_each_day_avg_focus_cnt,
		sum(case when action_type=6 then 1 else 0 end)/3 as user_3days_each_day_avg_click_cnt,
		
		count(distinct case when action_type=1 then sku_id else NULL end)/3 as user_3days_each_day_avg_browse_sku_cnt,
		count(distinct case when action_type=2 then sku_id else NULL end)/3 as user_3days_each_day_avg_add_cart_sku_cnt,
		count(distinct case when action_type=3 then sku_id else NULL end)/3 as user_3days_each_day_avg_del_cart_sku_cnt,
		count(distinct case when action_type=4 then sku_id else NULL end)/3 as user_3days_each_day_avg_order_sku_cnt,
		count(distinct case when action_type=5 then sku_id else NULL end)/3 as user_3days_each_day_avg_focus_sku_cnt,
		count(distinct case when action_type=6 then sku_id else NULL end)/3 as user_3days_each_day_avg_click_sku_cnt,
		
		count(distinct case when action_type=1 then action_brand else NULL end)/3 as user_3days_each_day_avg_browse_brand_cnt,
		count(distinct case when action_type=2 then action_brand else NULL end)/3 as user_3days_each_day_avg_add_cart_brand_cnt,
		count(distinct case when action_type=3 then action_brand else NULL end)/3 as user_3days_each_day_avg_del_cart_brand_cnt,
		count(distinct case when action_type=4 then action_brand else NULL end)/3 as user_3days_each_day_avg_order_brand_cnt,
		count(distinct case when action_type=5 then action_brand else NULL end)/3 as user_3days_each_day_avg_focus_brand_cnt,
		count(distinct case when action_type=6 then action_brand else NULL end)/3 as user_3days_each_day_avg_click_brand_cnt
		
	from dev.dev_temp_msj_risk_jdata_action_wide_table 
	where substring(action_time,1,10)>=date_sub('${current_date}',2) and substring(action_time,1,10)<='${current_date}' and action_cate = 6
	group by user_id
) user_3days_action
on user_month_action.user_id = user_3days_action.user_id
left outer join
(
	select user_id,
		sum(case when action_type=1 then 1 else 0 end) as user_5days_browse_cnt,
		sum(case when action_type=2 then 1 else 0 end) as user_5days_add_cart_cnt,
		sum(case when action_type=3 then 1 else 0 end) as user_5days_del_cart_cnt, 
		sum(case when action_type=4 then 1 else 0 end) as user_5days_order_cnt, 
		sum(case when action_type=5 then 1 else 0 end) as user_5days_focus_cnt,
		sum(case when action_type=6 then 1 else 0 end) as user_5days_click_cnt,
		
		sum(case when action_type=4 then 1 else 0 end)/sum(case when action_type=6 then 1 else 0 end) as user_5days_click_buy_rate,
		sum(case when action_type=2 then 1 else 0 end)/sum(case when action_type=6 then 1 else 0 end) as user_5days_click_cart_rate,
		sum(case when action_type=5 then 1 else 0 end)/sum(case when action_type=6 then 1 else 0 end) as user_5days_click_focus_rate,
		
		sum(case when action_type=4 then 1 else 0 end)/sum(case when action_type=1 then 1 else 0 end) as user_5days_browse_buy_rate,
		sum(case when action_type=4 then 1 else 0 end)/sum(case when action_type=2 then 1 else 0 end) as user_5days_cart_buy_rate,
		sum(case when action_type=4 then 1 else 0 end)/sum(case when action_type=5 then 1 else 0 end) as user_5days_focus_buy_rate,
		
		count(distinct case when action_type=1 then sku_id else NULL end) as user_5days_browse_sku_cnt,
		count(distinct case when action_type=2 then sku_id else NULL end) as user_5days_add_cart_sku_cnt,
		count(distinct case when action_type=3 then sku_id else NULL end) as user_5days_del_cart_sku_cnt,
		count(distinct case when action_type=4 then sku_id else NULL end) as user_5days_order_sku_cnt,
		count(distinct case when action_type=5 then sku_id else NULL end) as user_5days_focus_sku_cnt,
		count(distinct case when action_type=6 then sku_id else NULL end) as user_5days_click_sku_cnt,
		
		count(distinct case when action_type=1 then action_brand else NULL end) as user_5days_browse_brand_cnt,
		count(distinct case when action_type=2 then action_brand else NULL end) as user_5days_add_cart_brand_cnt,
		count(distinct case when action_type=3 then action_brand else NULL end) as user_5days_del_cart_brand_cnt,
		count(distinct case when action_type=4 then action_brand else NULL end) as user_5days_order_brand_cnt,
		count(distinct case when action_type=5 then action_brand else NULL end) as user_5days_focus_brand_cnt,
		count(distinct case when action_type=6 then action_brand else NULL end) as user_5days_click_brand_cnt,
		
		count(distinct case when action_type=1 then substring(action_time,1,10) else NULL end) as user_5days_browse_day_cnt,
		count(distinct case when action_type=2 then substring(action_time,1,10) else NULL end) as user_5days_add_cart_day_cnt,
		count(distinct case when action_type=3 then substring(action_time,1,10) else NULL end) as user_5days_del_cart_day_cnt,
		count(distinct case when action_type=4 then substring(action_time,1,10) else NULL end) as user_5days_order_day_cnt,
		count(distinct case when action_type=5 then substring(action_time,1,10) else NULL end) as user_5days_focus_day_cnt,
		count(distinct case when action_type=6 then substring(action_time,1,10) else NULL end) as user_5days_click_day_cnt,
		
		(5/count(distinct case when action_type=1 then substring(action_time,1,10) else NULL end)+0.1) as user_5days_avg_browse_interval_day,
		(5/count(distinct case when action_type=2 then substring(action_time,1,10) else NULL end)+0.1) as user_5days_avg_add_cart_interval_day,
		(5/count(distinct case when action_type=3 then substring(action_time,1,10) else NULL end)+0.1) as user_5days_avg_del_cart_interval_day,
		(5/count(distinct case when action_type=4 then substring(action_time,1,10) else NULL end)+0.1) as user_5days_avg_order_interval_day,
		(5/count(distinct case when action_type=5 then substring(action_time,1,10) else NULL end)+0.1) as user_5days_avg_focus_interval_day,
		(5/count(distinct case when action_type=6 then substring(action_time,1,10) else NULL end)+0.1) as user_5days_avg_click_interval_day,
		
		sum(case when action_type=1 then 1 else 0 end)/5 as user_5days_each_day_avg_browse_cnt,
		sum(case when action_type=2 then 1 else 0 end)/5 as user_5days_each_day_avg_add_cart_cnt,
		sum(case when action_type=3 then 1 else 0 end)/5 as user_5days_each_day_avg_del_cart_cnt, 
		sum(case when action_type=4 then 1 else 0 end)/5 as user_5days_each_day_avg_order_cnt, 
		sum(case when action_type=5 then 1 else 0 end)/5 as user_5days_each_day_avg_focus_cnt,
		sum(case when action_type=6 then 1 else 0 end)/5 as user_5days_each_day_avg_click_cnt,
		
		count(distinct case when action_type=1 then sku_id else NULL end)/5 as user_5days_each_day_avg_browse_sku_cnt,
		count(distinct case when action_type=2 then sku_id else NULL end)/5 as user_5days_each_day_avg_add_cart_sku_cnt,
		count(distinct case when action_type=3 then sku_id else NULL end)/5 as user_5days_each_day_avg_del_cart_sku_cnt,
		count(distinct case when action_type=4 then sku_id else NULL end)/5 as user_5days_each_day_avg_order_sku_cnt,
		count(distinct case when action_type=5 then sku_id else NULL end)/5 as user_5days_each_day_avg_focus_sku_cnt,
		count(distinct case when action_type=6 then sku_id else NULL end)/5 as user_5days_each_day_avg_click_sku_cnt,
		
		count(distinct case when action_type=1 then action_brand else NULL end)/5 as user_5days_each_day_avg_browse_brand_cnt,
		count(distinct case when action_type=2 then action_brand else NULL end)/5 as user_5days_each_day_avg_add_cart_brand_cnt,
		count(distinct case when action_type=3 then action_brand else NULL end)/5 as user_5days_each_day_avg_del_cart_brand_cnt,
		count(distinct case when action_type=4 then action_brand else NULL end)/5 as user_5days_each_day_avg_order_brand_cnt,
		count(distinct case when action_type=5 then action_brand else NULL end)/5 as user_5days_each_day_avg_focus_brand_cnt,
		count(distinct case when action_type=6 then action_brand else NULL end)/5 as user_5days_each_day_avg_click_brand_cnt
		
	from dev.dev_temp_msj_risk_jdata_action_wide_table 
	where substring(action_time,1,10)>=date_sub('${current_date}',4) and substring(action_time,1,10)<='${current_date}'  and action_cate = 6
	group by user_id
) user_5days_action
on user_month_action.user_id = user_5days_action.user_id
left outer join
(
	select user_id,
		sum(case when action_type=1 then 1 else 0 end) as user_7days_browse_cnt,
		sum(case when action_type=2 then 1 else 0 end) as user_7days_add_cart_cnt,
		sum(case when action_type=3 then 1 else 0 end) as user_7days_del_cart_cnt, 
		sum(case when action_type=4 then 1 else 0 end) as user_7days_order_cnt, 
		sum(case when action_type=5 then 1 else 0 end) as user_7days_focus_cnt,
		sum(case when action_type=6 then 1 else 0 end) as user_7days_click_cnt,
		
		sum(case when action_type=4 then 1 else 0 end)/sum(case when action_type=6 then 1 else 0 end) as user_7days_click_buy_rate,
		sum(case when action_type=2 then 1 else 0 end)/sum(case when action_type=6 then 1 else 0 end) as user_7days_click_cart_rate,
		sum(case when action_type=5 then 1 else 0 end)/sum(case when action_type=6 then 1 else 0 end) as user_7days_click_focus_rate,
		
		sum(case when action_type=4 then 1 else 0 end)/sum(case when action_type=1 then 1 else 0 end) as user_7days_browse_buy_rate,
		sum(case when action_type=4 then 1 else 0 end)/sum(case when action_type=2 then 1 else 0 end) as user_7days_cart_buy_rate,
		sum(case when action_type=4 then 1 else 0 end)/sum(case when action_type=5 then 1 else 0 end) as user_7days_focus_buy_rate,
		
		count(distinct case when action_type=1 then sku_id else NULL end) as user_7days_browse_sku_cnt,
		count(distinct case when action_type=2 then sku_id else NULL end) as user_7days_add_cart_sku_cnt,
		count(distinct case when action_type=3 then sku_id else NULL end) as user_7days_del_cart_sku_cnt,
		count(distinct case when action_type=4 then sku_id else NULL end) as user_7days_order_sku_cnt,
		count(distinct case when action_type=5 then sku_id else NULL end) as user_7days_focus_sku_cnt,
		count(distinct case when action_type=6 then sku_id else NULL end) as user_7days_click_sku_cnt,
		
		count(distinct case when action_type=1 then action_brand else NULL end) as user_7days_browse_brand_cnt,
		count(distinct case when action_type=2 then action_brand else NULL end) as user_7days_add_cart_brand_cnt,
		count(distinct case when action_type=3 then action_brand else NULL end) as user_7days_del_cart_brand_cnt,
		count(distinct case when action_type=4 then action_brand else NULL end) as user_7days_order_brand_cnt,
		count(distinct case when action_type=5 then action_brand else NULL end) as user_7days_focus_brand_cnt,
		count(distinct case when action_type=6 then action_brand else NULL end) as user_7days_click_brand_cnt,
		
		count(distinct case when action_type=1 then substring(action_time,1,10) else NULL end) as user_7days_browse_day_cnt,
		count(distinct case when action_type=2 then substring(action_time,1,10) else NULL end) as user_7days_add_cart_day_cnt,
		count(distinct case when action_type=3 then substring(action_time,1,10) else NULL end) as user_7days_del_cart_day_cnt,
		count(distinct case when action_type=4 then substring(action_time,1,10) else NULL end) as user_7days_order_day_cnt,
		count(distinct case when action_type=5 then substring(action_time,1,10) else NULL end) as user_7days_focus_day_cnt,
		count(distinct case when action_type=6 then substring(action_time,1,10) else NULL end) as user_7days_click_day_cnt,
		
		(7/count(distinct case when action_type=1 then substring(action_time,1,10) else NULL end)+0.1) as user_7days_avg_browse_interval_day,
		(7/count(distinct case when action_type=2 then substring(action_time,1,10) else NULL end)+0.1) as user_7days_avg_add_cart_interval_day,
		(7/count(distinct case when action_type=3 then substring(action_time,1,10) else NULL end)+0.1) as user_7days_avg_del_cart_interval_day,
		(7/count(distinct case when action_type=4 then substring(action_time,1,10) else NULL end)+0.1) as user_7days_avg_order_interval_day,
		(7/count(distinct case when action_type=5 then substring(action_time,1,10) else NULL end)+0.1) as user_7days_avg_focus_interval_day,
		(7/count(distinct case when action_type=6 then substring(action_time,1,10) else NULL end)+0.1) as user_7days_avg_click_interval_day,
		
		sum(case when action_type=1 then 1 else 0 end)/7 as user_7days_each_day_avg_browse_cnt,
		sum(case when action_type=2 then 1 else 0 end)/7 as user_7days_each_day_avg_add_cart_cnt,
		sum(case when action_type=3 then 1 else 0 end)/7 as user_7days_each_day_avg_del_cart_cnt, 
		sum(case when action_type=4 then 1 else 0 end)/7 as user_7days_each_day_avg_order_cnt, 
		sum(case when action_type=5 then 1 else 0 end)/7 as user_7days_each_day_avg_focus_cnt,
		sum(case when action_type=6 then 1 else 0 end)/7 as user_7days_each_day_avg_click_cnt,
		
		count(distinct case when action_type=1 then sku_id else NULL end)/7 as user_7days_each_day_avg_browse_sku_cnt,
		count(distinct case when action_type=2 then sku_id else NULL end)/7 as user_7days_each_day_avg_add_cart_sku_cnt,
		count(distinct case when action_type=3 then sku_id else NULL end)/7 as user_7days_each_day_avg_del_cart_sku_cnt,
		count(distinct case when action_type=4 then sku_id else NULL end)/7 as user_7days_each_day_avg_order_sku_cnt,
		count(distinct case when action_type=5 then sku_id else NULL end)/7 as user_7days_each_day_avg_focus_sku_cnt,
		count(distinct case when action_type=6 then sku_id else NULL end)/7 as user_7days_each_day_avg_click_sku_cnt,
		
		count(distinct case when action_type=1 then action_brand else NULL end)/7 as user_7days_each_day_avg_browse_brand_cnt,
		count(distinct case when action_type=2 then action_brand else NULL end)/7 as user_7days_each_day_avg_add_cart_brand_cnt,
		count(distinct case when action_type=3 then action_brand else NULL end)/7 as user_7days_each_day_avg_del_cart_brand_cnt,
		count(distinct case when action_type=4 then action_brand else NULL end)/7 as user_7days_each_day_avg_order_brand_cnt,
		count(distinct case when action_type=5 then action_brand else NULL end)/7 as user_7days_each_day_avg_focus_brand_cnt,
		count(distinct case when action_type=6 then action_brand else NULL end)/7 as user_7days_each_day_avg_click_brand_cnt
		
	from dev.dev_temp_msj_risk_jdata_action_wide_table 
	where substring(action_time,1,10)>=date_sub('${current_date}',6) and substring(action_time,1,10)<='${current_date}'  and action_cate = 6
	group by user_id
) user_7days_action
on user_month_action.user_id = user_7days_action.user_id
left outer join
(
	select user_id,
		sum(case when action_type=1 then 1 else 0 end) as user_10days_browse_cnt,
		sum(case when action_type=2 then 1 else 0 end) as user_10days_add_cart_cnt,
		sum(case when action_type=3 then 1 else 0 end) as user_10days_del_cart_cnt, 
		sum(case when action_type=4 then 1 else 0 end) as user_10days_order_cnt, 
		sum(case when action_type=5 then 1 else 0 end) as user_10days_focus_cnt,
		sum(case when action_type=6 then 1 else 0 end) as user_10days_click_cnt,
		
		sum(case when action_type=4 then 1 else 0 end)/sum(case when action_type=6 then 1 else 0 end) as user_10days_click_buy_rate,
		sum(case when action_type=2 then 1 else 0 end)/sum(case when action_type=6 then 1 else 0 end) as user_10days_click_cart_rate,
		sum(case when action_type=5 then 1 else 0 end)/sum(case when action_type=6 then 1 else 0 end) as user_10days_click_focus_rate,
		
		sum(case when action_type=4 then 1 else 0 end)/sum(case when action_type=1 then 1 else 0 end) as user_10days_browse_buy_rate,
		sum(case when action_type=4 then 1 else 0 end)/sum(case when action_type=2 then 1 else 0 end) as user_10days_cart_buy_rate,
		sum(case when action_type=4 then 1 else 0 end)/sum(case when action_type=5 then 1 else 0 end) as user_10days_focus_buy_rate,
		
		count(distinct case when action_type=1 then sku_id else NULL end) as user_10days_browse_sku_cnt,
		count(distinct case when action_type=2 then sku_id else NULL end) as user_10days_add_cart_sku_cnt,
		count(distinct case when action_type=3 then sku_id else NULL end) as user_10days_del_cart_sku_cnt,
		count(distinct case when action_type=4 then sku_id else NULL end) as user_10days_order_sku_cnt,
		count(distinct case when action_type=5 then sku_id else NULL end) as user_10days_focus_sku_cnt,
		count(distinct case when action_type=6 then sku_id else NULL end) as user_10days_click_sku_cnt,
		
		count(distinct case when action_type=1 then action_brand else NULL end) as user_10days_browse_brand_cnt,
		count(distinct case when action_type=2 then action_brand else NULL end) as user_10days_add_cart_brand_cnt,
		count(distinct case when action_type=3 then action_brand else NULL end) as user_10days_del_cart_brand_cnt,
		count(distinct case when action_type=4 then action_brand else NULL end) as user_10days_order_brand_cnt,
		count(distinct case when action_type=5 then action_brand else NULL end) as user_10days_focus_brand_cnt,
		count(distinct case when action_type=6 then action_brand else NULL end) as user_10days_click_brand_cnt,
		
		count(distinct case when action_type=1 then substring(action_time,1,10) else NULL end) as user_10days_browse_day_cnt,
		count(distinct case when action_type=2 then substring(action_time,1,10) else NULL end) as user_10days_add_cart_day_cnt,
		count(distinct case when action_type=3 then substring(action_time,1,10) else NULL end) as user_10days_del_cart_day_cnt,
		count(distinct case when action_type=4 then substring(action_time,1,10) else NULL end) as user_10days_order_day_cnt,
		count(distinct case when action_type=5 then substring(action_time,1,10) else NULL end) as user_10days_focus_day_cnt,
		count(distinct case when action_type=6 then substring(action_time,1,10) else NULL end) as user_10days_click_day_cnt,
		
		(10/count(distinct case when action_type=1 then substring(action_time,1,10) else NULL end)+0.1) as user_10days_avg_browse_interval_day,
		(10/count(distinct case when action_type=2 then substring(action_time,1,10) else NULL end)+0.1) as user_10days_avg_add_cart_interval_day,
		(10/count(distinct case when action_type=3 then substring(action_time,1,10) else NULL end)+0.1) as user_10days_avg_del_cart_interval_day,
		(10/count(distinct case when action_type=4 then substring(action_time,1,10) else NULL end)+0.1) as user_10days_avg_order_interval_day,
		(10/count(distinct case when action_type=5 then substring(action_time,1,10) else NULL end)+0.1) as user_10days_avg_focus_interval_day,
		(10/count(distinct case when action_type=6 then substring(action_time,1,10) else NULL end)+0.1) as user_10days_avg_click_interval_day,
		
		sum(case when action_type=1 then 1 else 0 end)/10 as user_10days_each_day_avg_browse_cnt,
		sum(case when action_type=2 then 1 else 0 end)/10 as user_10days_each_day_avg_add_cart_cnt,
		sum(case when action_type=3 then 1 else 0 end)/10 as user_10days_each_day_avg_del_cart_cnt, 
		sum(case when action_type=4 then 1 else 0 end)/10 as user_10days_each_day_avg_order_cnt, 
		sum(case when action_type=5 then 1 else 0 end)/10 as user_10days_each_day_avg_focus_cnt,
		sum(case when action_type=6 then 1 else 0 end)/10 as user_10days_each_day_avg_click_cnt,
		
		count(distinct case when action_type=1 then sku_id else NULL end)/10 as user_10days_each_day_avg_browse_sku_cnt,
		count(distinct case when action_type=2 then sku_id else NULL end)/10 as user_10days_each_day_avg_add_cart_sku_cnt,
		count(distinct case when action_type=3 then sku_id else NULL end)/10 as user_10days_each_day_avg_del_cart_sku_cnt,
		count(distinct case when action_type=4 then sku_id else NULL end)/10 as user_10days_each_day_avg_order_sku_cnt,
		count(distinct case when action_type=5 then sku_id else NULL end)/10 as user_10days_each_day_avg_focus_sku_cnt,
		count(distinct case when action_type=6 then sku_id else NULL end)/10 as user_10days_each_day_avg_click_sku_cnt,
		
		count(distinct case when action_type=1 then action_brand else NULL end)/10 as user_10days_each_day_avg_browse_brand_cnt,
		count(distinct case when action_type=2 then action_brand else NULL end)/10 as user_10days_each_day_avg_add_cart_brand_cnt,
		count(distinct case when action_type=3 then action_brand else NULL end)/10 as user_10days_each_day_avg_del_cart_brand_cnt,
		count(distinct case when action_type=4 then action_brand else NULL end)/10 as user_10days_each_day_avg_order_brand_cnt,
		count(distinct case when action_type=5 then action_brand else NULL end)/10 as user_10days_each_day_avg_focus_brand_cnt,
		count(distinct case when action_type=6 then action_brand else NULL end)/10 as user_10days_each_day_avg_click_brand_cnt
		
	from dev.dev_temp_msj_risk_jdata_action_wide_table 
	where substring(action_time,1,10)>=date_sub('${current_date}',9) and substring(action_time,1,10)<='${current_date}'  and action_cate = 6
	group by user_id
) user_10days_action
on user_month_action.user_id = user_10days_action.user_id
left outer join
(
	select user_id,
		sum(case when action_type=1 then 1 else 0 end) as user_15days_browse_cnt,
		sum(case when action_type=2 then 1 else 0 end) as user_15days_add_cart_cnt,
		sum(case when action_type=3 then 1 else 0 end) as user_15days_del_cart_cnt, 
		sum(case when action_type=4 then 1 else 0 end) as user_15days_order_cnt, 
		sum(case when action_type=5 then 1 else 0 end) as user_15days_focus_cnt,
		sum(case when action_type=6 then 1 else 0 end) as user_15days_click_cnt,
		
		sum(case when action_type=4 then 1 else 0 end)/sum(case when action_type=6 then 1 else 0 end) as user_15days_click_buy_rate,
		sum(case when action_type=2 then 1 else 0 end)/sum(case when action_type=6 then 1 else 0 end) as user_15days_click_cart_rate,
		sum(case when action_type=5 then 1 else 0 end)/sum(case when action_type=6 then 1 else 0 end) as user_15days_click_focus_rate,
		
		sum(case when action_type=4 then 1 else 0 end)/sum(case when action_type=1 then 1 else 0 end) as user_15days_browse_buy_rate,
		sum(case when action_type=4 then 1 else 0 end)/sum(case when action_type=2 then 1 else 0 end) as user_15days_cart_buy_rate,
		sum(case when action_type=4 then 1 else 0 end)/sum(case when action_type=5 then 1 else 0 end) as user_15days_focus_buy_rate,
		
		count(distinct case when action_type=1 then sku_id else NULL end) as user_15days_browse_sku_cnt,
		count(distinct case when action_type=2 then sku_id else NULL end) as user_15days_add_cart_sku_cnt,
		count(distinct case when action_type=3 then sku_id else NULL end) as user_15days_del_cart_sku_cnt,
		count(distinct case when action_type=4 then sku_id else NULL end) as user_15days_order_sku_cnt,
		count(distinct case when action_type=5 then sku_id else NULL end) as user_15days_focus_sku_cnt,
		count(distinct case when action_type=6 then sku_id else NULL end) as user_15days_click_sku_cnt,
		
		count(distinct case when action_type=1 then action_brand else NULL end) as user_15days_browse_brand_cnt,
		count(distinct case when action_type=2 then action_brand else NULL end) as user_15days_add_cart_brand_cnt,
		count(distinct case when action_type=3 then action_brand else NULL end) as user_15days_del_cart_brand_cnt,
		count(distinct case when action_type=4 then action_brand else NULL end) as user_15days_order_brand_cnt,
		count(distinct case when action_type=5 then action_brand else NULL end) as user_15days_focus_brand_cnt,
		count(distinct case when action_type=6 then action_brand else NULL end) as user_15days_click_brand_cnt,
		
		count(distinct case when action_type=1 then substring(action_time,1,10) else NULL end) as user_15days_browse_day_cnt,
		count(distinct case when action_type=2 then substring(action_time,1,10) else NULL end) as user_15days_add_cart_day_cnt,
		count(distinct case when action_type=3 then substring(action_time,1,10) else NULL end) as user_15days_del_cart_day_cnt,
		count(distinct case when action_type=4 then substring(action_time,1,10) else NULL end) as user_15days_order_day_cnt,
		count(distinct case when action_type=5 then substring(action_time,1,10) else NULL end) as user_15days_focus_day_cnt,
		count(distinct case when action_type=6 then substring(action_time,1,10) else NULL end) as user_15days_click_day_cnt,
		
		(15/count(distinct case when action_type=1 then substring(action_time,1,10) else NULL end)+0.1) as user_15days_avg_browse_interval_day,
		(15/count(distinct case when action_type=2 then substring(action_time,1,10) else NULL end)+0.1) as user_15days_avg_add_cart_interval_day,
		(15/count(distinct case when action_type=3 then substring(action_time,1,10) else NULL end)+0.1) as user_15days_avg_del_cart_interval_day,
		(15/count(distinct case when action_type=4 then substring(action_time,1,10) else NULL end)+0.1) as user_15days_avg_order_interval_day,
		(15/count(distinct case when action_type=5 then substring(action_time,1,10) else NULL end)+0.1) as user_15days_avg_focus_interval_day,
		(15/count(distinct case when action_type=6 then substring(action_time,1,10) else NULL end)+0.1) as user_15days_avg_click_interval_day,
		
		sum(case when action_type=1 then 1 else 0 end)/15 as user_15days_each_day_avg_browse_cnt,
		sum(case when action_type=2 then 1 else 0 end)/15 as user_15days_each_day_avg_add_cart_cnt,
		sum(case when action_type=3 then 1 else 0 end)/15 as user_15days_each_day_avg_del_cart_cnt, 
		sum(case when action_type=4 then 1 else 0 end)/15 as user_15days_each_day_avg_order_cnt, 
		sum(case when action_type=5 then 1 else 0 end)/15 as user_15days_each_day_avg_focus_cnt,
		sum(case when action_type=6 then 1 else 0 end)/15 as user_15days_each_day_avg_click_cnt,
		
		count(distinct case when action_type=1 then sku_id else NULL end)/15 as user_15days_each_day_avg_browse_sku_cnt,
		count(distinct case when action_type=2 then sku_id else NULL end)/15 as user_15days_each_day_avg_add_cart_sku_cnt,
		count(distinct case when action_type=3 then sku_id else NULL end)/15 as user_15days_each_day_avg_del_cart_sku_cnt,
		count(distinct case when action_type=4 then sku_id else NULL end)/15 as user_15days_each_day_avg_order_sku_cnt,
		count(distinct case when action_type=5 then sku_id else NULL end)/15 as user_15days_each_day_avg_focus_sku_cnt,
		count(distinct case when action_type=6 then sku_id else NULL end)/15 as user_15days_each_day_avg_click_sku_cnt,
		
		count(distinct case when action_type=1 then action_brand else NULL end)/15 as user_15days_each_day_avg_browse_brand_cnt,
		count(distinct case when action_type=2 then action_brand else NULL end)/15 as user_15days_each_day_avg_add_cart_brand_cnt,
		count(distinct case when action_type=3 then action_brand else NULL end)/15 as user_15days_each_day_avg_del_cart_brand_cnt,
		count(distinct case when action_type=4 then action_brand else NULL end)/15 as user_15days_each_day_avg_order_brand_cnt,
		count(distinct case when action_type=5 then action_brand else NULL end)/15 as user_15days_each_day_avg_focus_brand_cnt,
		count(distinct case when action_type=6 then action_brand else NULL end)/15 as user_15days_each_day_avg_click_brand_cnt
		
	from dev.dev_temp_msj_risk_jdata_action_wide_table 
	where substring(action_time,1,10)>=date_sub('${current_date}',14) and substring(action_time,1,10)<='${current_date}' and action_cate = 6
	group by user_id
) user_15days_action
on user_month_action.user_id = user_15days_action.user_id
