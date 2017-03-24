import { Component } from '@angular/core'
import { CategoryService} from './app.categories.service'
import { Category } from './app.category'
import { OnInit } from '@angular/core'

@Component({
    selector: "category-list",
    templateUrl:"./app.categorylist.html",
    styleUrls:["./app.category.css"],
    providers:[CategoryService]
})
export class CategoryListComponent implements OnInit{
    categories: Category[];
    constructor(private categoryService:CategoryService) {
        //this.categories = [new Category(1,'category')];
        
    }

    ngOnInit(){
        this.categoryService.getCategories()
            .subscribe(categorieslist=>{this.categories = categorieslist;},
                        error=>{});
    }
}