import sqlite3
import os
import datetime
#create sqllite database
db_file="todo_list.db"
conn=sqlite3.connect(db_file)
cursor=conn.cursor()
#craete a table to store tasks
cursor.execute("CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY,task_text TEXT NOT NULL,priority TEXT,due_date DATE,is_completed BOOLEAN)")
conn.commit()
def add_task(task_text,priority,due_date):
  cursor.execute("INSERT INTO tasks(task_text,priority,due_date,is_completed)VALUES(?,?,?,?)",(task_text,priority,due_date,False))
  conn.commit()
  print("Task addded succesfully")
def remove_task(task_id):
  cursor.execute("DELETE FROM tasks WHERE id=?",(task_id))
  conn.commit()
  print("Task marked as completed!")
def list_tasks():
  cursor.execute("SELECT * FROM tasks")
  tasks=cursor.fetchall()
  if not tasks:
    print("No tasks found")
  else:
    print("\n |D | Task    |Priority |Due Date  |Completed")
    print("-"*60)
    for task in tasks:
        for task in tasks:
             task_id, task_text, priority, due_date, is_completed = task
            
             print(f"{task_id:2}  | {task_text:24} | {priority:8} | {due_date or 'N/A':10} | {is_completed}")
       
def main():
     while True:
      print("/n options")
      print("1.Add Task")
      print("2.Remove Task")
      print("3.Mark Task as completed")
      print("4.list Tasks")
      print("5.exit")
      choice=input("eneter your choice:")
      if choice=="1":
       task_text=input("enter task description:")
       priority=input("Enter task prority (high/medium/low):")
       due_date_str=input("enter due date(YYYY-MM-DD,optional):")
       due_date=datetime.datetime.strptime(due_date_str,"%Y-%m-%d").date()
       add_task(task_text,priority,due_date)
      elif choice=="2":
          task_id=input("enter the ID of the task to remove:")
          remove_task(task_id)
      elif choice=="3":
           task_id=input("enter the id of the task to mark as complete:")
           mark_task_completed(task_id)
      elif choice=="4":
           list_tasks()
      elif choice=="5":
            conn.close()
            print("Goodbye!")
            break
      else:
             print("Invalid choice.please try again")
if __name__=="__main__":
     main()