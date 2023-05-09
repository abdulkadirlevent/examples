<?php

namespace App\Policies;

use App\Models\{_ModulName_};
use App\Models\User;
use Illuminate\Auth\Access\HandlesAuthorization;

class {_ModulName_}Policy
{{
    use HandlesAuthorization;

    /**
     * Determine whether the {_ModulNameLower_} can view any models.
     */
    public function viewAny(User $user): bool
    {{
        return $user->hasPermissionTo('list {_ModulNameLower_}');
    }}

    /**
     * Determine whether the {_ModulNameLower_} can view the model.
     */
    public function view(User $user, {_ModulName_} $model): bool
    {{
        return $user->hasPermissionTo('view {_ModulNameLower_}');
    }}

    /**
     * Determine whether the {_ModulNameLower_} can create models.
     */
    public function create(User $user): bool
    {{
        return $user->hasPermissionTo('create {_ModulNameLower_}');
    }}

    /**
     * Determine whether the {_ModulNameLower_} can update the model.
     */
    public function update(User $user, {_ModulName_} $model): bool
    {{
        return $user->hasPermissionTo('update {_ModulNameLower_}');
    }}

    /**
     * Determine whether the {_ModulNameLower_} can delete the model.
     */
    public function delete(User $user, {_ModulName_} $model): bool
    {{
        return $user->hasPermissionTo('delete {_ModulNameLower_}');
    }}

    /**
     * Determine whether the user can delete multiple instances of the model.
     */
    public function deleteAny(User $user): bool
    {{
        return $user->hasPermissionTo('delete {_ModulNameLower_}');
    }}

    /**
     * Determine whether the {_ModulNameLower_} can restore the model.
     */
    public function restore(User $user, {_ModulName_} $model): bool
    {{
        return false;
    }}

    /**
     * Determine whether the {_ModulNameLower_} can permanently delete the model.
     */
    public function forceDelete(User $user, {_ModulName_} $model): bool
    {{
        return false;
    }}
}}