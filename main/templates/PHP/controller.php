<?php

namespace App\Http\Controllers;

use App\Http\Resources\PermissionResource;
use App\Http\Resources\RoleResource;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\View\View;
use Inertia\Inertia;
use Inertia\Response;
use Laravel\Sanctum\Sanctum;
use Spatie\Permission\Models\Permission;
use Spatie\Permission\Models\Role;

class {_ModulName_}Controller extends Controller
{{
    /**
     * {_ModulName_} {_ModulNameLower_} index işlemi.
     */
    public function index(Request $request): Response
    {{
        $this->authorize('view-any', {_ModulName_}::class);

        ${_ModulNameLower_} = {_ModulName_}::all()->paginate(1000);

        return Inertia::render('{_ModulNameLower_}/Index', [
            '{_ModulNameLower_}' => {_ModulName_}Resource::collection(${_ModulNameLower_}),
            'search' =>'sss'
        ]);
    }}

    /**
     * Show the form for creating a new resource.
     */
    public function create(): Response
    {{
        $this->authorize('create', {_ModulName_}::class);

        return Inertia::render('{_ModulName_}/Create', [
            '{_ModulNameLower_}' => {_ModulName_}::all()
        ]);
    }}
}}