## **Database Architecture (Schema + Relations)** for the **Flask Student Portal**


## 📊 Entity Relationship Overview

### **1. Teacher**

| Field    | Type    | Notes                  |
| -------- | ------- | ---------------------- |
| id       | Integer | Primary Key            |
| username | String  | Unique                 |
| email    | String  | Unique, used for login |
| password | String  | Hashed                 |

---

### **2. StudentMark**

| Field       | Type    | Notes                                   |
| ----------- | ------- | --------------------------------------- |
| id          | Integer | Primary Key                             |
| roll        | Integer | Same student can have multiple subjects |
| name        | String  | Student name                            |
| gender      | String  | 'M' / 'F'                               |
| subject     | String  | One subject per entry                   |
| marks       | Integer | Out of 100 (or your preferred scale)    |
| teacher\_id | Integer | Foreign Key → `Teacher.id` (optional)   |

---

### ✅ Relationships

* **One teacher → many student entries**
* **One student (by roll no) → many subjects**
* `roll + subject` combo should be unique (enforced in logic)
* We do **not separate** student and subject tables to keep it flat/simple as per your requirement

---

## 🧩 ER Diagram (Text View)

```plaintext
+-------------+            +------------------+
|  Teacher    |◄───────────┤  StudentMark     |
+-------------+            +------------------+
| id (PK)     |        ┌───┤ id (PK)          |
| username    |        │   | roll             |
| email       |        │   | name             |
| password    |        │   | gender           |
+-------------+        │   | subject          |
                       │   | marks            |
                       └───| teacher_id (FK)  |
                           +------------------+
```

---

### 🔐 Constraints / Logic:

* `roll + subject` combo should be **unique per student**
* When updating student **name/gender**, apply to **all entries with that roll**
* `marks` are **per-subject per-student**
* Deleting all subject entries for a roll can mean deleting the student

---
