# NSQTech Internship Project – Role Based Login System

## 1. Problem Statement
In many applications, all admins have the same access. This project separates
Super Admin and Sub Admin roles to improve security and control.

## 2. Solution Overview
This is a Single Page Application built using Angular.
It provides:
- Login with role selection
- Role-based dashboard
- Super Admin with full permissions
- Sub Admin with limited permissions

## 3. Tech Stack
- Angular 12+
- TypeScript
- HTML, CSS
- RxJS (Observables)
- LocalStorage (session handling)

## 4. User Roles
### Super Admin
- View all users
- Edit user details
- Delete users

### Sub Admin
- View users
- ❌ Cannot edit
- ❌ Cannot delete

### General User
- View own records only

## 5. Application Flow
Login → Role Check → Dashboard → Permission-based Actions

## 6. Key Files Explained
- `login.component.ts` – Handles login & session
- `dashboard.component.ts` – Role-based UI & permissions
- `user.service.ts` – Fake backend (user data)

## 7. How Permissions Are Controlled
Permissions are checked using the user role stored in localStorage.

## 8. How to Run the Project
1. npm install
2. ng serve
3. Open http://localhost:4200

## 9. Future Improvements
- JWT authentication
- Real backend integration
- Unit testing
