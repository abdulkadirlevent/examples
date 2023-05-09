<?php

namespace App\Models;

use App\Models\Scopes\Searchable;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\SoftDeletes;

class Cari extends Model
{
    use HasFactory;
    use Searchable;
    use SoftDeletes;

    /**
     * Cari cari Modelinde görünmesini istediğiniz alanları doldurun.
     * @example ['id', 'name']
     */
    protected $fillable = []

    protected $searchableFields = ['*'];
}