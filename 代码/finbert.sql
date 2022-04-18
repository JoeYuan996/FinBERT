use finbert;
#'2021-10-12','hello world',1
insert into finbert.commentlog(id,ctime,content,label) values(1,'2021-10-12','hello world',1);
DELIMITER $
CREATE PROCEDURE UPD(IN ctime varchar(50),IN com varchar(256),IN label int,out res int) 
BEGIN
	
	insert into finbert.commentlog(ctime,content,label) values(ctime,com,label);
    SET res=1;
END$
DELIMITER ;
SELECT * FROM finbert.commentlog;
CALL UPD('2021-12-12','hello world',1,@res);
DROP PROCEDURE  IF EXISTS UPD;
select @res

DELIMITER $
CREATE EVENT drop_old  ON SCHEDULE  every 1 day
DO
BEGIN
	
	DELETE FROM finbert.commentlog where datediff(curdate(),ctime)>7;
    #INSERT into commentlog(ctime,content,label) values(new.ctime,new.content,new.label);
END$
DELIMITER ;
SELECT * FROM finbert.commentlog;
#select datediff(curdate(),date('2021-03-18'))
DROP EVENT IF EXISTS drop_old;
#SHOW VARIABLES LIKE 'event_scheduler';
#set GLOBAL event_scheduler = 1；
SHOW CREATE TABLE commentlog;