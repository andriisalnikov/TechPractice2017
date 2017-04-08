import { Routes } from "@angular/router";
import { CompetitionListComponent } from './competitions/app.competitionlist'
import { CategoryListComponent } from './categories/app.categorylist'

export class ApplicationRoutes {
    public static routes: Routes = [
        {
            path:'',
            component: CompetitionListComponent
        },
        {
            path:'categories/:id',
            component: CategoryListComponent
        }
    ]
}