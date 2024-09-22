<?php

//******************************************************************************
//
// fields : db name, html name, html title, maxlen, editable

// id field
define('_id_', 'id');

// table name
define('_tbl_name_', 'data');

// field metadata indices
define('_fld_name_', 0);
define('_fld_fld_',  1);
define('_fld_head_', 2);
define('_fld_len_',  3);
define('_fld_edit_', 4);

// field metadata
$fields
  = array
  (
    array ( _id_,       _id_  , 'Id'             ,    0, false ),
    array ( 'name', 'nm', 'Name',   100, true  ),
    array ( 'author',       'aut'  , 'Author'             ,   100, true  ),
    array ( 'theatre',   'the', 'Theatre'         ,  100, true  ),
    array ( 'performance',  'per', 'Perfomance'        , 100, true  ),
    array ( 'quantity_of_acts',   'quan', 'Quantity of acts'         ,  100, true  ),
    array ( 'ticket_price',  'tick', 'Ticket price'        , 100, true  ),
    array ( 'music',   'mus', 'Music'         ,  1, true  )
  );

//******************************************************************************
//
// database queries

define('_tbls_show_', 'show tables');

define('_tbl_make_', '
create table `' . _tbl_name_ . '`
(
  `id`       bigint(20)    not null,
  `name` varchar(100) not null,
  `author`       varchar(100)   not null,
  `theatre`   varchar(100)  not null,
  `performance`  varchar(100) not null,
  `quantity_of_acts`   smallint  not null,
  `ticket_price`  bigint  not null,
  `music`   boolean  not null,
  primary key (`id`)
)
engine=myisam
default charset=utf8;
');

define('_tbl_drop_', 'drop table `' . _tbl_name_ . '`');

define('_tbl_wipe_', 'delete from `' . _tbl_name_ . '`');

define('_tbl_seed_', "
insert into `" . _tbl_name_ . "` (`" . $fields[0][_fld_name_] . "`, `" . $fields[1][_fld_name_] . "`, `" . $fields[2][_fld_name_] . "`, `" . $fields[3][_fld_name_] . "`, `" . $fields[4][_fld_name_] . "`, `" . $fields[5][_fld_name_] . "`, `" . $fields[6][_fld_name_] . "`, `" . $fields[7][_fld_name_] . "`) values
(1, 'SORCERY_POTION', 'Oleksandr_Melnyk', 'Theater_on_Podil','3/12/2022','4','200','1' ),
(2, 'SNOW_IN_APRIL', 'Taras_Kravchenko', 'Theater_19','10/10/2023','4','150','1'),
(3, 'OVERCOAT', 'Maksym_Oliynyk', 'Theater_of_Taras','2/6/2023','2','125','0'),
(4, 'DREAMS_COME_TO_LIFE', 'George_Bondar', 'Academic_Theater_of_Les_Kurbas','2/16/2022','6','375','0'),
(5, 'OBSERVER', 'Vasyl_Rudenko', 'Theater_on_Chinay_19','24/12/2023','5','230','1');
");

define('_tbl_insrepl_', ' into `' . _tbl_name_ . '` (`id`, `name`, `author`, `theatre`, `performance`, `quantity_of_acts`,`ticket_price`,`music`) values (?, ?, ?, ?, ?, ?, ?, ?)');

define('_tbl_insert_', 'insert' . _tbl_insrepl_);

define('_tbl_replace_', 'replace' . _tbl_insrepl_);

define('_tbl_delete_', 'delete from `' . _tbl_name_ . '` where `id` = ?');

define('_tbl_select_', 'select * from `' . _tbl_name_ . '` order by `id`');

//******************************************************************************
//
// returns mysqli or stmt error

function show_error ( $mysqli, $stmt = null )
{
  if ( ! $stmt )
    if ( $mysqli->connect_errno )
      return 'error ' . $mysqli->connect_errno . ' connecting to db :' . '<br>' . $mysqli->connect_error;
    else
      return 'error ' . $mysqli->errno . ' executing query :' . '<br>' . $mysqli->error;
  else
    return 'error ' . $stmt->errno . ' executing query :' . '<br>' . $stmt->error;
}

//******************************************************************************

?>
