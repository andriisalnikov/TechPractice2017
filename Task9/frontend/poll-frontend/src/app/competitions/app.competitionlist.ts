import { Component } from '@angular/core'
import { CompetitionService } from './app.competition.service'
import { Competition } from './app.competition'
import { OnInit } from '@angular/core'

@Component({
    selector: "competition-list",
    templateUrl: "./app.competitionlist.html",
    styleUrls: ["./app.competition.css"],
    providers: [CompetitionService]
})
export class CompetitionListComponent implements OnInit {
    competitions: Competition[];
    constructor(private competitionService: CompetitionService) {

    }

    ngOnInit() {
        this.competitionService.getCategories()
            .subscribe(competitionslist => { this.competitions = competitionslist; },
            error => { });
    }
}