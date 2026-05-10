import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { delay } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class DashboardService {

  getAdminRecords(): Observable<any[]> {
    return of([
      { id: 1, name: 'User One', role: 'USER' },
      { id: 2, name: 'User Two', role: 'USER' },
      { id: 3, name: 'Admin', role: 'ADMIN' },
      { id: 4, name: 'Super Admin', role: 'SuperAdmin' }
    ]).pipe(delay(2000)); // API delay simulation
  }

  getUserRecords(): Observable<any[]> {
    return of([
      { id: 101, task: 'Verify profile' },
      { id: 102, task: 'Upload documents' }
    ]).pipe(delay(1500));
  }
}
