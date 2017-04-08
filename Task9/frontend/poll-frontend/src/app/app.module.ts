import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterModule, Routes} from "@angular/router"

import { AppComponent } from './app.component';
import { CategoryListComponent } from './categories/app.categorylist';
import { CategoryService } from './categories/app.categories.service';
import { CompetitionListComponent } from './competitions/app.competitionlist'
import { ApplicationRoutes } from "./app.routes"

@NgModule({
  declarations: [
    AppComponent,
    CategoryListComponent,
    CompetitionListComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    RouterModule.forRoot(ApplicationRoutes.routes)
  ],
  providers: [CategoryService],
  bootstrap: [AppComponent]
})
export class AppModule { }
