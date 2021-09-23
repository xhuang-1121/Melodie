# README
[![Build status](https://app.travis-ci.com/SongminYu/Melodie.svg?token=qNTghqDqnwadzvj4y4z7&branch=master&status=passed)](https://travis-ci.com/SongminYu)

This project is supposed to be developed as a general framework that can be used to establish agent-based models for specific uses. Current main contributors are **Songmin YU** and **Zhanyi HOU**. 



#### 1 Meetings

- 20210707 - Brief exchange of development ideas
- 20210806 - Brief exchange about mesa and agentpy, and the plan of project
- 2021082x - Discuss classes design and their interaction (UML)



#### 2 Current Step

##### Songmin

- design classes and their interaction

##### Zhanyi

- travis
- codecov
- cookie-cutter



#### 3 Ideas


#### 4 Manager

run this command in project root:
```cmd
python -m Melodie serve
```
and visit this website:

http://localhost:8089/

The webpage will provide a simple database viewer with two selection widgets.
The one shows all database files in the path where you run this command and its
sub-folders, and the other shows all tables of current selected database.

This page loads the whole table data when you switch table, but only renders 
several rows instead of rendering them all. So in most cases there will be no worry
about performance.

![img.png](docs/source/.images/melodiemanager-sqliteview.png)


