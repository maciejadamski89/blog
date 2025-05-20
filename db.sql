drop table if exists posts;
create table posts (
    id integer primary key auto_increment,
    title text not null,
    content text not null,
    created_at timestamp not null default current_timestamp,
    updated_at timestamp not null default current_timestamp on update current_timestamp
)
