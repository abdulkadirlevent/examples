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

class CariController extends Controller
{
    /**
     * Cari cari index işlemi.
     */
    public function index(Request $request): Response
    {
        $this->authorize('view-any', Cari::class);

        $cari = Cari::all()->paginate(1000);

        return Inertia::render('cari/Index', [
            'cari' => CariResource::collection($cari),
            'search' =>'sss'
        ]);
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create(): Response
    {
        $this->authorize('create', Cari::class);

        return Inertia::render('Cari/Create', [
            'cari' => Cari::all()
        ]);
    }
}