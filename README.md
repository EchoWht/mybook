## Python Flask 


参考文档
flask中文文档
http://docs.jinkan.org/docs/flask/

SQLAlchemy使用笔记－－SQLAlchemy ORM（一）
http://blog.csdn.net/billvsme/article/details/50197197

廖大神的 使用SQLAlchemy
http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320114981139589ac5f02944601ae22834e9c521415000


Beautiful Soup 4.2.0 文档¶
https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id5

imooc 爬虫教程
http://www.imooc.com/video/10687

坑点一：
flask 是跑在 virtualenv（虚拟环境）上的，所以sqlalchemy也要装在virtualenv上，切记
坑点二：
文档上文件上传路径是绝对路径，例如"/static/file/"
而在我的环境中需要会报错文件夹找不到，而我改成相对路径就可以了
UPLOAD_FOLDER = "static/file/"

updateMybook


获取某个对象所有的属性
        print(dir(Object))
Query' object  attribute '

['_Query__all_equivs', '__class__', '__clause_element__', '__delattr__', '__dict
__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__lt__'
, '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
'__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_ada
pt_all_clauses', '_adapt_clause', '_adapt_col_list', '_adapt_polymorphic_element
', '_adjust_for_single_inheritance', '_attributes', '_autoflush', '_bind_mapper'
, '_clone', '_compile_context', '_compound_eager_statement', '_conditional_optio
ns', '_connection_from_session', '_correlate', '_criterion', '_current_path', '_
distinct', '_enable_assertions', '_enable_eagerloads', '_enable_single_crit', '_
entities', '_entity_zero', '_execute_and_instances', '_execution_options', '_fil
ter_aliases', '_for_update_arg', '_from_obj', '_from_obj_alias', '_from_selectab
le', '_get_bind_args', '_get_condition', '_get_existing_condition', '_get_impl',
 '_get_options', '_group_by', '_has_mapper_entities', '_having', '_invoke_all_ea
gers', '_join', '_join_entities', '_join_left_to_right', '_join_to_left', '_join
path', '_joinpoint', '_joinpoint_zero', '_limit', '_mapper_adapter_map', '_mappe
r_entities', '_mapper_loads_polymorphically_with', '_mapper_zero', '_no_clauseel
ement_condition', '_no_criterion_assertion', '_no_criterion_condition', '_no_lim
it_offset', '_no_statement_condition', '_no_yield_per', '_offset', '_only_entity
_zero', '_only_full_mapper_zero', '_only_load_props', '_options', '_order_by', '
_orm_only_adapt', '_orm_only_from_obj_alias', '_params', '_polymorphic_adapters'
, '_populate_existing', '_prefixes', '_prepare_right_side', '_primary_entity', '
_query_entity_zero', '_refresh_state', '_reset_joinpoint', '_reset_polymorphic_a
dapter', '_select_args', '_select_from_entity', '_set_enable_single_crit', '_set
_entities', '_set_entity_selectables', '_set_select_from', '_should_log_debug',
'_should_log_info', '_should_nest_selectable', '_simple_statement', '_statement'
, '_suffixes', '_update_joinpoint', '_values', '_version_check', '_with_current_
path', '_with_hints', '_with_invoke_all_eagers', '_with_labels', '_with_options'
, '_yield_per', 'add_column', 'add_columns', 'add_entity', 'all', 'as_scalar', '
autoflush', 'column_descriptions', 'correlate', 'count', 'cte', 'delete', 'dispa
tch', 'distinct', 'enable_assertions', 'enable_eagerloads', 'except_', 'except_a
ll', 'execution_options', 'exists', 'filter', 'filter_by', 'first', 'from_self',
 'from_statement', 'get', 'group_by', 'having', 'instances', 'intersect', 'inter
sect_all', 'join', 'label', 'limit', 'logger', 'merge_result', 'offset', 'one',
'one_or_none', 'options', 'order_by', 'outerjoin', 'params', 'populate_existing'
, 'prefix_with', 'reset_joinpoint', 'scalar', 'select_entity_from', 'select_from
', 'selectable', 'session', 'slice', 'statement', 'subquery', 'suffix_with', 'un
ion', 'union_all', 'update', 'value', 'values', 'whereclause', 'with_entities',
'with_for_update', 'with_hint', 'with_labels', 'with_lockmode', 'with_parent', '
with_polymorphic', 'with_session', 'with_statement_hint', 'with_transformation',
 'yield_per']

