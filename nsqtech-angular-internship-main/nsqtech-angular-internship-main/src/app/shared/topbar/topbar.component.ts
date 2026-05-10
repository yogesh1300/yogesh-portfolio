import { Component, EventEmitter, Output } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-topbar',
  standalone: true,
  templateUrl: './topbar.component.html'
})
export class TopbarComponent {
  @Output() logoutEvent = new EventEmitter<void>();

  constructor(private router: Router) {}

  logout() {
    this.logoutEvent.emit();
  }

  goHome() {
    this.router.navigate(['/dashboard']);
  }
}
