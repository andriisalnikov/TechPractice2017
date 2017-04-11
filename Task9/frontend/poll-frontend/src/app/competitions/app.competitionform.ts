import { Component } from '@angular/core'
import { CompetitionService } from './app.competition.service'
import { Competition } from './app.competition'
import { OnInit } from '@angular/core'

@Component({
    selector: "competition-form",
    templateUrl: "./app.competitionform.html",
    styleUrls: ["./app.competition.css"],
    providers: [CompetitionService]
})
export class CompetitionFormComponent implements OnInit {
    public competition: Competition;
    constructor(private competitionService: CompetitionService) {
        this.competition = new Competition(0,"");
    }
    createCompetition():void {

    }
    ngOnInit() {
        
    }
}