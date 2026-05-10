import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  login(userId: string, password: string, role: string) {
    const user = { userId, role };
    localStorage.setItem('user', JSON.stringify(user));
  }

  getUser() {
    return JSON.parse(localStorage.getItem('user') || '{}');
  }

  logout() {
    localStorage.removeItem('user');
  }
}
