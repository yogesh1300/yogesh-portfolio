import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  username: string = '';
  password: string = '';
  role: string = '';
  isLoading: boolean = false;
  errorMessage: string = '';

  constructor(private router: Router) {}

  onLogin() {
    this.errorMessage = '';
    this.isLoading = true;

    // No delay, instant login check
    this.isLoading = false;
    if (this.username && this.password && this.role) {
      // Store user in localStorage
      localStorage.setItem('user', JSON.stringify({ username: this.username, role: this.role }));
      // Navigate to dashboard
      this.router.navigate(['/dashboard']);
    } else {
      this.errorMessage = 'Please fill all the fields';
    }
  }
}
