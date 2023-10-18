# In preparation - Drop the DB and Users

DROP DATABASE IF EXISTS `xxx_ictprg431`;

# % allows ANY location to connect - SERIOUS security issue
DROP USER IF EXISTS `xxx_ictprg431_user`@`%`;
# 127.0.0.1 is the IPv4 address for your local computer
DROP USER IF EXISTS `xxx_ictprg431_user`@`127.0.0.1`;
# Domain name based access
drop user if exists `xxx_ictprg431_user`@`sea-otter.local`;

FLUSH PRIVILEGES;


# No create DB and USER and Give permissions

CREATE DATABASE IF NOT EXISTS `xxx_ictprg431`;

CREATE USER IF NOT EXISTS `xxx_ictprg431_user`@`127.0.0.1` IDENTIFIED BY 'Myword1';
GRANT ALL ON `xxx_ictprg431`.* TO `xxx_ictprg431_user`@`127.0.0.1`;
GRANT USAGE ON *.* TO `xxx_ictprg431_user`@`127.0.0.1`;


FLUSH PRIVILEGES;