import { CanActivateFn, Router } from '@angular/router';
import { inject } from '@angular/core';

export const adminGuard: CanActivateFn = () => {
  const router = inject(Router);
  const userData = localStorage.getItem('user');

  if (!userData) {
    router.navigate(['']);
    return false;
  }

  const user = JSON.parse(userData);

  // Allow both Admin and SuperAdmin to access admin routes
  if (user.role === 'Admin' || user.role === 'SuperAdmin') {
    return true;
  }

  router.navigate(['/user']);
  return false;
};
