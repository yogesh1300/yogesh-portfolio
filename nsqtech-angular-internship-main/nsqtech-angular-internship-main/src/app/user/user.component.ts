import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DashboardService } from '../services/dashboard.service';

@Component({
  selector: 'app-user',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './user.component.html'
})
export class UserComponent implements OnInit {

  tasks: any[] = [];
  loading = true;

  constructor(private dashboard: DashboardService) {}

  ngOnInit(): void {
    this.dashboard.getUserRecords().subscribe((data: any[]) => {
      this.tasks = data;
      this.loading = false;
    });
  }
}
