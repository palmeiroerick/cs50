create table users (
    `id` int auto_increment,
    `first_name` varchar(32) not null,
    `last_name` varchar(32) not null,
    `username` varchar(32) not null unique,
    `password` varchar(128) not null,
    primary key(`id`)
);

create table schools (
    `id` int auto_increment,
    `name` varchar(32) not null,
    `type` enum('Primary', 'Secondary', 'Higher Education') not null,
    `location` varchar(32) not null,
    `founded` date not null,
    primary key(`id`)
);

create table companies (
    `id` int auto_increment,
    `name` varchar(32) not null,
    `industry` enum('Technology', 'Education', 'Business') not null,
    `location` varchar(32) not null,
    primary key(`id`)
);

create table people_connections (
    `id` int auto_increment,
    `user_id` int,
    `following_id` int,
    primary key(`id`),
    foreign key(`user_id`) references `users`(`id`),
    foreign key(`following_id`) references `users`(`id`)
);

create table school_connections (
    `id` int auto_increment,
    `user_id` int,
    `school_id` int,
    `start_date` date not null,
    `end_date` date,
    `degree_type` varchar(32) not null,
    primary key(`id`),
    foreign key(`user_id`) references `users`(`id`),
    foreign key(`school_id`) references `schools`(`id`)
);

create table company_connections (
    `id` int auto_increment,
    `user_id` int,
    `company_id` int,
    `start_date` date not null,
    `end_date` date,
    primary key(`id`),
    foreign key(`user_id`) references `users`(`id`),
    foreign key(`company_id`) references `companies`(`id`)
);
