import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TopbarComponent } from '../shared/topbar/topbar.component';
import { UserService } from '../services/user.service';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule, TopbarComponent, FormsModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  user: any;
  records: any[] = [];
  users: any[] = [];
  isLoading = true;
  editingUserId: string | null = null;
  editedName = '';
  editedRole = '';

  constructor(
    private userService: UserService,
    private router: Router
  ) {}

  ngOnInit() {
    const storedUser = localStorage.getItem('user');

    if (!storedUser) {
      this.router.navigate(['/login']);
      return;
    }

    this.user = JSON.parse(storedUser);
    this.loadRecords();

    // ✅ Admin + SuperAdmin can VIEW users
    if (this.user.role === 'Admin' || this.user.role === 'SuperAdmin') {
      this.loadUsers();
    }
  }

  private loadRecords() {
    this.userService.getUserRecords(this.user.role).subscribe({
      next: (data) => {
        this.records = data;
        this.isLoading = false;
      },
      error: () => {
        this.isLoading = false;
      }
    });
  }

  private loadUsers() {
    this.userService.getAllUsers().subscribe({
      next: (data) => {
        this.users = data;
      }
    });
  }

  onLogout() {
    localStorage.removeItem('user');
    this.router.navigate(['/login']);
  }

  // ✅ Only SuperAdmin can edit
  startEdit(user: any) {
    if (this.user?.role !== 'SuperAdmin') {
      alert('Only Super Admin can edit users.');
      return;
    }

    this.editingUserId = user.id;
    this.editedName = user.username;
    this.editedRole = user.role;
  }

  // ✅ Only SuperAdmin can save edit
  saveEdit(user: any) {
    if (this.user?.role !== 'SuperAdmin') return;

    this.userService.editUser(user.id, {
      username: this.editedName,
      role: this.editedRole
    }).subscribe(() => {
      this.editingUserId = null;
      this.loadUsers();
    });
  }

  cancelEdit() {
    this.editingUserId = null;
    this.editedName = '';
    this.editedRole = '';
  }

  // ✅ Only SuperAdmin can delete
  deleteUser(userId: string) {
    if (this.user?.role !== 'SuperAdmin') {
      alert('Only Super Admins can delete users.');
      return;
    }

    if (confirm('Are you sure you want to delete this user?')) {
      this.userService.deleteUser(userId).subscribe(() => {
        this.loadUsers();
      });
    }
  }
}