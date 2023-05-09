<?php

namespace App\Policies;

use App\Models\Cari;
use App\Models\User;
use Illuminate\Auth\Access\HandlesAuthorization;

class CariPolicy
{
    use HandlesAuthorization;

    /**
     * Determine whether the cari can view any models.
     */
    public function viewAny(User $user): bool
    {
        return $user->hasPermissionTo('list cari');
    }

    /**
     * Determine whether the cari can view the model.
     */
    public function view(User $user, Cari $model): bool
    {
        return $user->hasPermissionTo('view cari');
    }

    /**
     * Determine whether the cari can create models.
     */
    public function create(User $user): bool
    {
        return $user->hasPermissionTo('create cari');
    }

    /**
     * Determine whether the cari can update the model.
     */
    public function update(User $user, Cari $model): bool
    {
        return $user->hasPermissionTo('update cari');
    }

    /**
     * Determine whether the cari can delete the model.
     */
    public function delete(User $user, Cari $model): bool
    {
        return $user->hasPermissionTo('delete cari');
    }

    /**
     * Determine whether the user can delete multiple instances of the model.
     */
    public function deleteAny(User $user): bool
    {
        return $user->hasPermissionTo('delete cari');
    }

    /**
     * Determine whether the cari can restore the model.
     */
    public function restore(User $user, Cari $model): bool
    {
        return false;
    }

    /**
     * Determine whether the cari can permanently delete the model.
     */
    public function forceDelete(User $user, Cari $model): bool
    {
        return false;
    }
}