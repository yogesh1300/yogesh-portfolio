import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { delay } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  // ✅ Added SuperAdmin user
  private users = [
    { id: '1', username: 'superadmin', password: 'superadmin', role: 'SuperAdmin' },
    { id: '2', username: 'admin', password: 'admin', role: 'Admin' },
    { id: '3', username: 'user', password: 'user', role: 'General User' }
  ];

  constructor(private http: HttpClient) {}

  login(username: string, password: string, role: string): Observable<any> {
    const user = this.users.find(u => u.username === username && u.password === password && u.role === role);
    if (user) {
      return of(user).pipe(delay(1000)); // Simulate API delay
    }
    return of(null);
  }

  getAllUsers(): Observable<any[]> {
    return of(this.users);
  }

  getUserRecords(role: string): Observable<any[]> {
    const records = role === 'Admin' ? [
      { id: 1, name: 'Admin Record 1' },
      { id: 2, name: 'Admin Record 2' }
    ] : role === 'SuperAdmin' ? [
      { id: 1, name: 'SuperAdmin Record 1' },
      { id: 2, name: 'SuperAdmin Record 2' },
      { id: 3, name: 'SuperAdmin Record 3' }
    ] : [
      { id: 1, name: 'User Record 1' }
    ];
    return of(records).pipe(delay(500)); // Simulate API delay
  }

  editUser(id: string, updatedUser: any): Observable<any> {
    const index = this.users.findIndex(u => u.id === id);
    if (index !== -1) {
      this.users[index] = { ...this.users[index], ...updatedUser };
      return of(this.users[index]);
    }
    return of(null);
  }

  deleteUser(id: string): Observable<any> {
    this.users = this.users.filter(u => u.id !== id);
    return of(true);
  }
}