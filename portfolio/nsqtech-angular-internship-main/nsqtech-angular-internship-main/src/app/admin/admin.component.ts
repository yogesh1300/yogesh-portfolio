import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DashboardService } from '../services/dashboard.service';

@Component({
  selector: 'app-admin',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './admin.component.html'
})
export class AdminComponent implements OnInit {

  users: any[] = [];
  loading = true;

  constructor(private dashboard: DashboardService) {}

  ngOnInit(): void {
    this.dashboard.getAdminRecords().subscribe((data: any[]) => {
      this.users = data;
      this.loading = false;
    });
  }
}
