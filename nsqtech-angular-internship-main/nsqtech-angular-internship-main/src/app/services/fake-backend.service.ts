import { Injectable } from '@angular/core';

export interface User {
  username: string;
  role: string;
  status: string;
}

@Injectable({ providedIn: 'root' })
export class FakeBackendService {
  private users: User[] = [
    { username: 'Ravi', role: 'User', status: 'Active' },
    { username: 'Anu', role: 'User', status: 'Inactive' },
    { username: 'Admin', role: 'Admin', status: 'Active' },
    { username: 'Super', role: 'SuperAdmin', status: 'Active' } // added SuperAdmin
  ];

  login(username: string, password: string, role: string) {
    // return user object directly
    return { username, role };
  }

  getUsers() {
    return new Promise<User[]>(resolve => {
      setTimeout(() => {
        resolve(this.users);
      }, 1200); // simulate delay
    });
  }

  deleteUser(username: string) {
    this.users = this.users.filter(u => u.username !== username);
    return new Promise(resolve => setTimeout(() => resolve(true), 500));
  }

  editUser(username: string, newData: Partial<User>) {
    const user = this.users.find(u => u.username === username);
    if (user) Object.assign(user, newData);
    return new Promise(resolve => setTimeout(() => resolve(true), 500));
  }
}
